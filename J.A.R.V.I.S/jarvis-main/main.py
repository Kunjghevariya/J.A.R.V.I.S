import os
import eel

from engine.features import *

eel.init("www")

playAssistantSound()



os.system('start msedge.exe --app="http://localhost:8000/index.html"')

eel.start('index.html', mode=None, host='localhost', block=True)

def main():
    speak("Hello, I am Jarvis")
    wish_me()
    while True:
        print("Listening...")
        query = take_command().lower()

        if "open youtube" in query:
            open_website("https://www.youtube.com")
        elif "open google" in query:
            open_website("https://www.google.com")
        elif "open my website" in query:
            speak("Opening your website, Sir")
            os.system("start file:///C:/Users/Admin1/Desktop/personal%20website/index.html")
        elif "time" in query:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {current_time}")
        elif "wikipedia" in query:
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif "search youtube".lower() in query:
            query = query.replace("search youtube", "")
            speak("Searching YouTube for " + query)
            pywhatkit.playonyt(query)
            speak("I hope you find what you were looking for, Sir")
        elif "open in chrome".lower() in query.lower() :
            query = query.replace("jarvis", "")
            query = query.replace("open in chrome", "")
            speak("Searching  for " + query)
            open_website("https://www." + query)
            
        elif "exit" in query:
            speak("Goodbye, Sir")
            exit()