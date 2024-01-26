from bardapi import BardCookies
import speech_recognition as sr
import os
import pyttsx3
import pywhatkit
import datetime


cookie_dict = {
    "__Secure-1PSID" : "eQinMNgz00ULw5fE_RnYwan3_hpvSoBTunnf_wU0GTs9j6zHz82NW745tIFUKFBg_xTafw.",
    "__Secure-1PSIDTS" : "sidts-CjIBPVxjShSmwRfxyvdZSbWRZvzJio9nzR5qIhunjTQEZMOPUzxXtg51SVqk19-8m-f2VBAA",
    "__Secure-1PSIDCC" : "ABTWhQHHi_K3kE9ULsQ6PO8s9DjrZj7t0qwD6rU1qXMB3N24tX3a-YDbXdppEOmfuSyFom2KLRg"
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

# Main Execution

while True:
    Question = input("Enter The Query : ")
    RealQuestion = str(Question)
    results = bard.get_answer(RealQuestion)['content']
    current_datetime = datetime.datetime.now()
    formatted_time = current_datetime.strftime("%H%M%S")
    filenamedate = str(formatted_time) + str(".txt")
    filenamedate = "DataBase//" + filenamedate
    print(split_and_save_paragraphs(results, filename=filenamedate))
