from os import startfile
from pyautogui import click
from keyboard import press
from keyboard import write
from time import sleep
import webbrowser as web

def whatsappmsg(name,message) :
    #startfile("C:\\Program Files\\VideoLAN\\VLC\\vlc.exe")
    web.open("https://web.whatsapp.com/")
    sleep(7)
    click(x=244, y=204)
    sleep(0.5)
    write(name)
    sleep(1)
    click(x=408, y=350)
    sleep(0.5)
    click(x=766, y=991)
    sleep(0.5)
    write(message)
    press('enter')
    sleep(60)
