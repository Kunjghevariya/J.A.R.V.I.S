from bardapi import BardCookies
import speech_recognition as sr
import os
import pyttsx3
import pywhatkit
import datetime


cookie_dict = {
    "__Secure-1PSID" : "bginMABr3NWSwUYYSen2L2xaHwAS-Hj4-TcoTdYt_mL3gb84jiGSA15o926TlwXEJXjmAw.",
    "__Secure-1PSIDTS" : "sidts-CjIB3e41hZFhJZEtUyE_86pVXkwAGALmcJj50Swd9wIICU2oHGBFBo_tfbGHQXEOzMv1sRAA",
    "__Secure-1PSIDCC" : "ACA-OxN6P82DUkwKs6KDjvF8h824bXB_vj_dhUvtWCEEY-59SAn_rCrnTAyhOMnHxxaXLTqjRao"
}




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
    imagename = str(input("Enter The Image Name : "))
    image = open(imagename,'rb').read()
    bard = BardCookies(cookie_dict=cookie_dict)
    results = bard.ask_about_image('what is in the image?',image=image)['content']
    current_datetime = datetime.datetime.now()
    formatted_time = current_datetime.strftime("%H%M%S")
    filenamedate = str(formatted_time) + str(".txt")
    filenamedate = "DataBase//" + filenamedate
    print(split_and_save_paragraphs(results, filename=filenamedate))



