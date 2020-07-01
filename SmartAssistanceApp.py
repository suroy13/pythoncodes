from tkinter import messagebox
from VirtualAssistanceApp_UI import MyWindow
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib,ssl
import pyaudio
from email.mime.multipart import MIMEMultipart

# Variable declarations
botname="David"
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
def wishMe():
    """This Function written to greet the User"""
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        messagebox.showinfo('Message title', 'Good Morning!')

    elif hour>=12 and hour<18:
        messagebox.showinfo('Message title', 'Good Afternoon!')

    else:
        messagebox.showinfo('Message title', 'Good Evening!')

    messagebox.showinfo('Usage Instructions', 'Please type in the keyword for which you want to perform task!')


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('ajit.royc@gmail.com', 'Watermelon2188')
    server.sendmail('ajit.royc@gmail.com', to, content)
    server.close()



def initiate_events():
    wishMe()
    #while True:
    if 1:
     inputa=MyWindow.inputstrng
     query =inputa.upper()

    # Logic for executing tasks based on query
    if 'WIKIPEDIA' in query:
        messagebox.showinfo('SmartAssistanceApp Says', 'wikipedia')


    # Open youtube .com
    elif 'YOUTUBE' in query:
        messagebox.showinfo('SmartAssistanceApp Says', 'Youtube.com has been initiated!, Enjoy Your Videos!')
        webbrowser.get(chrome_path).open("youtube.com")

        # speak("Youtube.com has been opened Successfully!, Enjoy Your Videos! Thank for Using me.")
    # Open Google .com





