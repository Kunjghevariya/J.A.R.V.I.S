from playsound import playsound
import speech_recognition as sr
import os
import pyttsx3
import webbrowser as web
import datetime
import wikipedia
import pywhatkit


# Playing assiatnt sound function
def playAssistantSound():
    music_dir = "www\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)

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
        return "error"

def open_website(url):
    speak(f"Opening {url} Sir")
    web.open(url)