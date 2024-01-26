

import pyttsx3
import speech_recognition as sr
import datetime

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
# print(voice[1].id)
engine.setProperty('voice',voice[0].id)


def speak(audio):
   engine.say(audio)
   engine.runAndWait()
   
   
def  wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
        
    elif hour>=12 and hour<18:  
        speak("Good Afternoon!")
        
    else:
        speak("Good Evening!")
           
    
    speak("i am jarvis sir. plesae tell me how may i help you")
    
def takecommand():
    
    r =sr.Recognizer()
    with sr.Microphone() as source:
       print("listeing...")
    r.pause_threshold = 1
    audio =r.listen(source)
                 
                 
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n") 
        return query 

    except Exception as e:  
        # print(e) 
        print("say that again please...") 
        return "error"
    
if __name__ == "__main__":
    wishme()
   
               
