import speech_recognition as sr
import os
import pyttsx3
import webbrowser as web
import datetime
import wikipedia
import pywhatkit
from bardapi import BardCookies

cookie_dict = {
    "__Secure-1PSID" : "bginMABr3NWSwUYYSen2L2xaHwAS-Hj4-TcoTdYt_mL3gb84jiGSA15o926TlwXEJXjmAw.",
    "__Secure-1PSIDTS" : "sidts-CjIB3e41ha-t_RD6Uc2NxeJMfWdHQ-PorTCi4Vfk-4qJ1UW0bd-06BrqfrYeK5pnsUYRPBAA",
    "__Secure-1PSIDCC" : "ACA-OxOAf5xIdOGpnSJ52sGLTyLAnLzrLx6_JOIOLX24jBKuJ2aCTCu4UzZpmDOCNm4UB7uXGFA"
}

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def wish_me():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis Sir. Please tell me how may I help you")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User Said: {query}")
        return query
    except Exception as e:
        print(f"Error: {e}")
        return "hello"

def open_website(url):
    speak(f"Opening {url} Sir")
    web.open(url)

def main():
    speak("Hello, I am Jarvis")
    wish_me()
    while True:
                print("Listening...")
                query = take_command().lower()

   
                print("Listening google...")
                RealQuestion = str(query)
                print(RealQuestion)
                results = bard.get_answer(RealQuestion)['content']
                current_datetime = datetime.datetime.now()
                formatted_time = current_datetime.strftime("%H%M%S")
                filenamedate = str(formatted_time) + str(".txt")
                filenamedate = "DataBase//" + filenamedate
                print(split_and_save_paragraphs(results, filename=filenamedate))
                speak(split_and_save_paragraphs(results, filename=filenamedate))
                
                if "exit" in query:
                    speak("Goodbye, Sir")
                    exit()
                    
if __name__ == "__main__":
    main()