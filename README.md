
# GUI Based ChatBot <span style= "color:rgb(190,100,195)"> RePaLK</span>

Introducing the PyQT5 GUI-based Chatbot named RePaLK powered by the cutting-edge Open AI GPT-3.5 Turbo model.
This innovative application seamlessly combines the power of advanced natural language processing with a user-friendly interface, enhancing both information retrieval and interactive communication. 

The chatbot features a dual-window design that optimizes user experience and functionality. 

The first window serves as an open platform for dynamic prompts. 
Users can initiate conversations by typing in queries, seeking advice, or engaging in casual interactions. 
The GPT-3.5 Turbo model responds with human-like coherence, offering valuable insights and informative responses.

The second window introduces a novel dimension to the chatbot capabilities. 
Here, users are empowered to upload PDF files, unlocking a new level of document-specific inquiries. 
With a user-friendly upload feature, the chatbot delves into the contents of the uploaded PDF, comprehending the textual information within. 
Users can then pose context-aware questions related to the PDFs content. 
The chatbot responses are tailored to the document's specifics, providing accurate answers and insightful summaries.

The synergy between the GPT-3.5 Turbo model and the PyQt5 interface creates a fluid and intuitive interaction. 
Users can seamlessly switch between windows, utilizing the chatbot for both general inquiries and document-specific research. 
This fusion of technology and user-centric design transforms information retrieval into an engaging and efficient process.
 
The intuitive layout empowers users of varying technical proficiencies to effortlessly navigate and leverage the chatbot capabilities. 
Whether it's a casual conversation or an in-depth exploration of PDF documents, the chatbot offers a versatile toolset catering to diverse user needs.
In essence, the GUI-based chatbot with the GPT-3.5 Turbo model and dual-window functionality represents a leap forward in user-centric AI applications.


## Requirements
```bash
Python==3.x.x
Pyqt5
SpeechRecognition
pyttsx4
pyaudio
OpenAI
LangChain
```
## Installation

1. Clone and navigate to RePaLk directory.
2. Create virtual environment and activate it before packages installations.

```bash
python -m venv myvenv
```
```for Windows```
```bash
./myvenv/Script/activate
```
``` for linux```
```bash
source myvenv/bin/activate [for linux]
``` 

3. Install the required packages.

```bash
pip install -r requirements.txt
```
4. Open [.env](https://github.com/sarnav38/RePaLk/blob/main/.env) file and enter OpenAI_API key and 
api_key for daily news from News Api (optional).

5. Go to the clone directory and run.

```bash
python app.py
```    

![App Screenshot](https://github.com/sarnav38/RePaLk/blob/main/assests/run_app.PNG)

5. You're done and let's chat and talk with your RePaLK.

## Authentication OpenAI
>  **Warning** Do not expose the ```api_key```
1. open Edge browser Visit https://platform.openai.com/
2. Login with your Account. Once you log in you will be taken to the Profile page.
3. Goto Personal --> View API keys --> create new secret key. Copy and paste in .env file.

## Authentication NewsAPi
**Warning** Do not expose the ```api_key```
1. visit and login in to https://newsapi.org/
2. Click on APi key button and copy api key in paste in config.json file.

## Usage RePaLK
1. Application Usage and shortcut keys instruction in Mouse tip Window and Switching between Main window and Your Data chat Window

![App Screenshot](https://github.com/sarnav38/RePaLk/blob/main/assests/instruction.gif)

## Usage Window 1
1. Enter the prompt by typing and press enter to get response from bot.

![App Screenshot](https://github.com/sarnav38/RePaLk/blob/main/assests/mainWindow.gif)

2. Enter the voice prompt by click on mic button and pressed till command shown on the output window.

![App Screenshot](https://github.com/sarnav38/RePaLk/blob/main/assests/listen%20prompt.gif)

3. Save the response by clicking on it and then click button save as a file to save response. Press Clear button to Clear output window.

![App Screenshot](https://github.com/sarnav38/RePaLk/blob/main/assests/saveClear.gif)

## Usage Window 2
1. upload PDF or txt files and ask document-specific inquiries.

![App Screenshot](https://github.com/sarnav38/RePaLk/blob/main/assests/fileUpload.gif)

## Prompt Examples

1. ```open google.com``` command to open google.com
see [config.json](https://github.com/sarnav38/RePaLk/blob/main/config.json) file for other website to be open by ```open websitename``` command.

2. ```Generate code``` and save file.

![App Screenshot](https://github.com/sarnav38/RePaLk/blob/main/assests/code.gif)

3. ```open chat analyser``` to open [whatsapp chat analyser ML model](https://whatsapchatanz.streamlit.app).

4. ```open crick``` to open [T20 IPL Predition ML model](https://cricpred.streamlit.app).

5. ``` today date ``` 

![App Screenshot](https://github.com/sarnav38/RePaLk/blob/main/assests/dateCommand.gif)

## Author

- [Arnav Sharma](https://www.github.com/sarnav38)
