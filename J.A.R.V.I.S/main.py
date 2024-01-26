import speech_recognition as sr
import os
import pyttsx3
import webbrowser as web
import datetime
import wikipedia
import pywhatkit
from bardapi import BardCookies
from geopy.distance import great_circle
from geopy.geocoders  import Nominatim
import geocoder
import requests

cookie_dict = {
    "__Secure-1PSID" : "eQinMNgz00ULw5fE_RnYwan3_hpvSoBTunnf_wU0GTs9j6zHz82NW745tIFUKFBg_xTafw.",
    "__Secure-1PSIDTS" : "sidts-CjIBPVxjShSmwRfxyvdZSbWRZvzJio9nzR5qIhunjTQEZMOPUzxXtg51SVqk19-8m-f2VBAA",
    "__Secure-1PSIDCC" : "ABTWhQHHi_K3kE9ULsQ6PO8s9DjrZj7t0qwD6rU1qXMB3N24tX3a-YDbXdppEOmfuSyFom2KLRg"
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
        speak("hmm")
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

def My_Location():

    

    speak("Checking....")


    ip_add = requests.get('https://api.ipify.org').text

    url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'

    geo_q = requests.get(url)

    geo_d = geo_q.json()

    city = geo_d['city']
    
    state = geo_d['region']
    
    timezone = geo_d['timezone']

    country = geo_d['country']
    
    op = "https://www.google.com/maps/place/" + city
    web.open(op)
    
    print(f"Sir , You Are Now In {city, state , country} and You Time zone was {timezone}.")

    speak(f"Sir , You Are Now In {city, state , country} and You Time zone was {timezone}.")

def GoogleMaps(Place):

    Url_Place = "https://www.google.com/maps/place/" + str(Place)

    geolocator = Nominatim(user_agent="myGeocoder")

    location = geolocator.geocode(Place , addressdetails= True)

    target_latlon = location.latitude , location.longitude

    web.open(url=Url_Place)

    location = location.raw['address']

    target = {'city' : location.get('city',''),
                'state' : location.get('state',''),
                'country' : location.get('country','')}

    current_loca = geocoder.ip('me')

    current_latlon = current_loca.latlng

    distance = str(great_circle(current_latlon,target_latlon))
    distance = str(distance.split(' ',1)[0])
    distance = round(float(distance),2)


    speak(target)
    speak(f"Sir , {Place} iS {distance} Kilometre Away From Your Location . ")
    
    
    
def main():
    speak("Initializing Jarvis")

    speak("All drivers are up and running")
    speak("All systems have been activated")
    speak("Now I am online")
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
        elif 'whatsapp message' in query:

            name = query.replace("whatsapp message","")
            name = name.replace("send ","")
            name = name.replace("to ","")
            Name = str(name)
            speak(f"Whats The Message For {Name}")
            MSG = take_command()
            from Automations import whatsappmsg
            whatsappmsg(Name,MSG)
            
        elif 'my location' in query :
            My_Location()
            
        elif 'where is' in query :
            Place = query.replace("where is ","")
            Place = Place.replace("jarvis" , "")
            GoogleMaps(Place)
            
        elif "exit" in query:
            speak("Goodbye, Sir")
            exit()
            
        elif "google" in query :
            print("Google Bard Is started")
            speak("Google Bard Is started")
            bard = BardCookies(cookie_dict=cookie_dict)

            def split_and_save_paragraphs(data, filename):
                paragraphs = data.split('\n\n')
                with open(filename, 'w') as file:
                    file.write(data)
                data = paragraphs[:2]
                separator = ', '
                joined_string = separator.join(data)
                return joined_string

            

            while True:
                print("Listening google...")
                query = take_command().lower()
                
               
                RealQuestion = str(query)
                
                
                results = bard.get_answer(RealQuestion)['content']
                
                current_datetime = datetime.datetime.now()
                formatted_time = current_datetime.strftime("%H%M%S")
                filenamedate = str(formatted_time) + str(".txt")
                filenamedate = "DataBase//" + filenamedate
                filenamedate = filenamedate.replace("*" ,"")
                print(split_and_save_paragraphs(results, filename=filenamedate))
                speak(split_and_save_paragraphs(results, filename=filenamedate))
                
                if "exit" in query:
                    speak("Goodbye, Sir")
                    exit()
                    
if __name__ == "__main__":
    main()