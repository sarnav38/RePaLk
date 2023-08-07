import datetime, json, wikipedia, webbrowser, os, pyttsx4
from winPyFiles.location import getIpLoc, getLogLat
# from bardapi import Bard
from winPyFiles.newTop5 import topNews
import speech_recognition as sr
import openai
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

openai.api_key = os.environ['OPENAI_API_KEY']

# token = os.environ['SSID']

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(model=model, messages=messages, temperature=temperature)
    return response.choices[0].message["content"]

def mySpeak(audio: str) -> None:
    """It will Speak whatsoever string you pass to it"""
    engine = pyttsx4.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 20)
    engine.say(audio)
    engine.runAndWait()


def takeCommand() -> str:
    """It will take microphone input and return string output"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        mySpeak("Listening")
        r.pause_threshold = 0.5
        audio = r.listen(source)
    # // using google recognizer for said speech
    try:
        query = r.recognize_google(audio)
        mySpeak("Recognizing command")
        return query
    except Exception:
        mySpeak(' mySpeak again as command not recognizing')
        return ""

def returnQuery(query: str) -> str:

    try:
        with open('config.json', 'r', encoding='utf-8') as f:
            software = json.load(f)['software']
    except Exception:
        nosoft = 'No software data in config.json file or config.json file not exsit'
        mySpeak(nosoft)
        return nosoft

    try:
        with open('config.json', 'r', encoding='utf-8') as f:
            brws = json.load(f)['browser']
            chrome_path = brws[1]
            webbrowser.register(brws[0], None, webbrowser.BackgroundBrowser(chrome_path))
            browser = webbrowser.get(brws[0])
    except Exception:
        brsoft = 'No browser name and its path in config.json file or config.json file not exsit'
        mySpeak(brsoft)
        # return brsoft

    try:
        with open('config.json', 'r', encoding='utf-8') as f:
            sites = json.load(f)['sites']
    except Exception:
        sidta = 'config.json file not exsit or data in sites not exits'
        mySpeak(sidta)
        return sidta

    # TODO sites opening
    try:
        for site in sites:
            if f'open {site[0]}' in query:
                mySpeak(f'Opening {site[0]}')
                browser.open(f'{site[1]}')
                return f'Opening {site[0]}'
    except Exception:
        si = 'check Internet connection slow or '
        mySpeak(si)
        return si

    # TODO software opening
    try:
        for soft in software:
            if f'open {soft[0]}' in query:
                mySpeak(f'Opening {soft[0]}')
                os.startfile(soft[1])
                return f'Opening {soft[0]}'
    except Exception:
        sofr = 'enter software and its path as per your pc '
        mySpeak(sofr)
        return sofr

    # TODO exit app
    if 'exit' in query:
        exit(0)

    # TODO news headlines
    elif 'top headlines' in query:
        try:
            top5news = topNews()
            data = ''
            for index, news in enumerate(top5news):
                data = data + f'Headlines number {index + 1} {news["title"]} \n {news["url"]} \n'
            return data
        except Exception:
            da = 'Enter you own api key in file api_key.txt or check internet connection'
            mySpeak(da)
            return da

    # TODO wiki
    elif 'wikipedia' in query:
        try:
            mySpeak("Searching wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5)
            mySpeak("According to wikipedia")
            return results
        except Exception:
            wiki = 'Check your Internet connection'
            mySpeak(wiki)
            return wiki

    # TODO time
    elif 'time' in query:
        strtime = datetime.datetime.now().strftime('%H:%M:%S')
        mySpeak(f"sir, the time is {strtime}")
        return strtime

    # TODO date
    elif 'today date' in query:
        strdate = datetime.datetime.now().strftime('%d:%B:%Y')
        mySpeak(f"sir, the date is {strdate}")
        return strdate

    # TODO location
    elif 'location coordinates for' in query:
        try:
            query = query.replace('location coordinates for', '').strip()
            b = getLogLat(query)
            mySpeak(b)
            return b
        except Exception:
            mySpeak('Wrong Location Input given')
            return 'Wrong Location Input given'

    # TODO ip
    elif 'ip address location for' in query:
        try:
            query = query.replace('ip address location for', '').strip()
            a = getIpLoc(query)
            mySpeak(a)
            return a
        except Exception:
            mySpeak('Wrong Ip address Input given')
            return 'Wrong Ip address Input given'

    # TODO bard
    else:
        try:
            messages = [
                {'role': 'system',
                 'content': 'You are a polite Ai assistant '},
                {'role': 'user',
                 'content': f'{query}'},
            ]
            # bard = Bard(token=token)
            # res = bard.get_answer(query)['content']
            mySpeak("Searching prompt")
            mySpeak("According to ChatBot")
            res = get_completion_from_messages(messages)
            return res
        except Exception:
            mySpeak('Wrong API Key entered or Check Internet connection.')
            return 'Wrong API Key entered or Check Internet connection.'


