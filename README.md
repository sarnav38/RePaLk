
# GUI Based ChatBot Powered By Bard Ai

A GUI based chatbot build using python3.8 and pyqt5 powered by bard ai, wikipedia search, browser search and many more. 


## Requirements
```bash
Python==3.x.x
Pyqt5
SpeechRecognition
pyttsx4
pyaudio
GoogleBard
```
## Installation

1. Clone and navigate to RePaLk directory.
2. Install the required packages.

```bash
pip install -r requirements.txt
```
3. Open config.json file and enter Google Bard. See Authentication section below to get SSID and api_key for daily news from News Api (optional).

4. Go to the clone directory and run.

```bash
./myvenv/Script/activate
python app.py
```    
![App Screenshot](https://github.com/sarnav38/RePaLk/blob/main/assests/run_app.PNG)

5. You're done and let's chat and talk with your RePaLK.

## Authentication Bard
>  **Warning** Do not expose the ```__Secure-1PSID```
1. open Edge browser Visit https://bard.google.com/
2. F12 for console
3.  Session: Application → Cookies → Copy the value of __Secure-1PSID cookie and paste in config.json file.

![App Screenshot](https://via.placeholder.com/400x50?text=App+Screenshot+Here)

## Authentication NewsAPi
**Warning** Do not expose the ```api_key```
1. visit and login in to https://newsapi.org/
2. Click on APi key button and copy api key in paste in config.json file.

## Usage

1. Enter the prompt by typing and press enter to get response from bot.
![App Screenshot](https://via.placeholder.com/400x50?text=App+Screenshot+Here)

2. Enter the voice prompt by click on mic button and pressed till command shown on the output window.
![App Screenshot](https://via.placeholder.com/400x50?text=App+Screenshot+Here)

3. Save the respone by clicking on it and then click button save as a file to save response.

4. Press Clear button to Clear output window.
![App Screenshot](https://via.placeholder.com/400x50?text=App+Screenshot+Here)
## Prompt Examples

1. ```open google.com``` command to open google.com.
see config.json file for other website to be be open by ```open websitename``` command.

2. Generate code 

![App Screenshot](https://via.placeholder.com/400x50?text=App+Screenshot+Here)

3. ```open chat analyser``` to open whatsapp chat anaylyser ML model.
url: https://whatsapchatanz.streamlit.app/

4. ```open crick``` to open T20 IPL Predition ML model.
url: https://cricpred.streamlit.app/

## Author

- [Arnav Sharma](https://www.github.com/sarnav38)

