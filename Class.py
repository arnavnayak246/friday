#PRE-REQUISITES!!-
#1. Open Command Prompt
#2. Run the Following Commands.
#3. pip install pyttsx3
#4. pip install pyaudio
#5. pip install wikipedia
#6. pip install speechrecognition
#7. pip install webbrowser
# ONCE YOU HAVE FINISHED,RUN THE BELOW CODE 
import wikipedia
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import os
assistant = pyttsx3.init('sapi5')
voices = assistant.getProperty('voices')
print(voices)
assistant.setProperty('voice',voices[4].id)
assistant.setProperty('rate',184)

def speak(audio):
    assistant.say(audio)
    assistant.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12 :
        speak("good Morning I am FRIDAY created by Arnaav . I am a simple python A I . I can handle simple tasks . Try saying COVID 19 according to wikipedia")
    elif hour>=12 and hour<14 :
        speak("good Afternoon I am FRIDAY created by Arnaav . I am a simple python A I . I can handle simple tasks . Try saying COVID 19 according to wikipedia")
    else:
        speak("good evening I am FRIDAY created by Arnaav . I am a simple python A I . I can handle simple tasks . Try saying COVID 19 according to wikipedia")

def takeCommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening..")
        command.pause_threshold = 1
        audio = command.listen(source)

        try:
            print("recogn..")
            query = command.recognize_google(audio,language='en-in')
            print(f"you said :{query}")

        except Exception as Error:
            return "none"
        return query.lower()

def openApp(): 
        os.startfile('pushpa.mp3')
        
     
if __name__ == "__main__":
    wishMe()
    
while True:
    query = takeCommand()
#TRY SAYING "COVID-19 ACCORDING TO WIKIPEDIA".
#TRY SAYING "PLAY MUSIC".
#TRY SAYING "WHERE IS STATUE OF LIBERTY".
    if "wikipedia"in query:
        speak("finding results!!!")
        answer = query.replace("according to wikipedia","")
        answer = query.replace("in wikipedia","")
        answer = query.replace("wikipedia", "")
        wiki = wikipedia.summary(answer,2)
        assistant.setProperty('rate',166)
        print(wiki)
        speak(f"wikipedia says:{wiki}")
        assistant.setProperty('rate',187)

    elif "music" in query:
        speak ("Playing a Music for you")    
        openApp()

      
    elif "where is " in query:
        query = query.replace("where is","")
        urll = 'https://earth.google.com/web/search/'+query
        vari = query
        speak("finding "+vari+" on the Map")
        webbrowser.open(urll)
        print("0")
        print("1")
        print("2")
        print("0")
        print("1")
        print("2")
        print("0")
        print("1")
        print("2")
        speak("sir! , i found the exact coordinates of this place!!!!!!!!!!!!!!!!!")
        wiki = wikipedia.summary(vari,4)
        assistant.setProperty('rate',166)
        print(vari)
        speak(query+wiki)
        assistant.setProperty('rate',187)     