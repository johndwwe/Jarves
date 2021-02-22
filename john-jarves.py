import os # import os
import pyttsx3 # spking pip install pyttsx3
import datetime # use to no date time
import speech_recognition as sr # pip install SpeechRecognition
import subprocess # pip install subprocess
import wikipedia # pip install wikipedia

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def login():
    pass

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%p")
    speak(Time)

def date():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Wellcome john Dcosta")
    speak("the current time is")
    time()
    speak("the current date is")
    date()
    hour = datetime.datetime.now().hour
    if hour >=6 and hour<12:
        speak("Good night bro!")
    elif hour >=12 and hour<18:
        speak("Good afternon bro!")
    elif hour >=18 and hour<24:
        speak("Good Evening bro!")
    else:
        speak("Good morning bro!")
    speak("it's me")
    speak("Amanda")
    speak("at your service.")
    speak("please tell me how can i help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recongnizning...")
        query = r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        print(e)

        return "None"
    return query

wishme()

while True:
    query = takeCommand().lower()
    if 'wikipedia' in query:
        speak("Searching wikipedia...")
        query = query.replace("wikipedia", "")
        result = wikipedia.summary(query, sentences=4)
        speak("four sentences i will tell you")
        print(result)
        speak(result)
    elif 'bye' in query:
        speak("bye bye bro")
        exit()
    elif 'exit' in query:
        speak("bye bye bro")
        exit()
    elif 'open browser' in query:
        speak('which browser')
        speak('chrome. or')
        speak('Microsoft edge')
    elif 'open chrome' in query:
        speak('chrome is opening')
        chrome = subprocess.Popen(['C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'])
    elif 'close chrome' in query:
        speak('closeing chrome')
        chrome.terminate()
    elif 'open microsoft edge' in query:
        speak('microsoft Edge is opening')
        microsoft = subprocess.Popen(['C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe'])
    elif 'close microsoft edge' in query:
        speak('microsoft Edge is closeing')
        microsoft.terminate()
    elif 'open youtube' in query:
        speak('youtube is opening')
        youtube = subprocess.Popen(['C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe', 'youtube.com'])
    elif 'close youtube' in query:
        speak('closeing youtube')
        youtube.terminate()
    elif 'open google' in query:
        speak('google is opening')
        google = subprocess.Popen(['C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe', 'google.com'])
    elif 'close google' in query:
        speak('close google')
        google.terminate()
    elif 'what is your name' in query:
        speak('my name is amanda')
    elif 'your name' in query:
        speak('my name is amanda')
    elif 'what your name' in query:
        speak('my name is amanda')
    elif 'open notepad' in query:
        speak('opening notepad')
        notepad = subprocess.Popen(['C:\\Windows\\system32\\notepad.exe'])
    elif 'close notepad' in query:
        speak('closeing notepad')
        notepad.terminate()
    elif 'close' in query:
        speak('bye bye john')
        exit()