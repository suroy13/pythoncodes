import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib,ssl
import pyaudio
from email.mime.multipart import MIMEMultipart

# Variable declarations demo
botname="David"
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    """This Function written to speak the audion used by the BOT"""
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    """This Function written to greet the User"""
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I  am  "+botname+" ,  created by Subhankar Roy. How may I help you today!!")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("Recognizing...")
        speak('Recognizing your inputs please wait........!')
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        speak('Sorry, say that again please ..')
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('ajit.royc@gmail.com', 'Watermelon2188')
    server.sendmail('ajit.royc@gmail.com', to, content)
    server.close()



if __name__ == "__main__":
    wishMe()
    while True:
    #if 1:
        query = takeCommand().lower()

# Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
# Open youtube .com
        elif 'open youtube' in query:
            webbrowser.get(chrome_path).open("youtube.com")
            speak("Youtube.com has been opened Successfully!, Enjoy Your Videos! Thank for Using me.")
#Open Google .com
        elif 'open google' in query:
            webbrowser.get(chrome_path).open("google.com")
            speak("Google.com has been opened Successfully!, Thank for Using me.")
#Open Netflix app
        elif 'open netflix' in query:
            os.system('start Netflix:')
            speak("Netflix has been opened Successfully!, Enjoy the movie.")
# Open one cognizant.com
        elif 'one cognizant' in query:
            webbrowser.get(chrome_path).open("https://onecognizant.cognizant.com/")
            speak("1C has been opened Successfully!, you may need to authenticate yourself as per your Company Policy!")

# close chrome browser session
        elif 'close chrome' in query:
            try:
                os.system("taskkill /im chrome.exe /f")
                speak("All Sessions of Chrome browser has been closed Successfully!, Thank for Using me.")
            except Exception as e:
                # print(e)
                speak("All the Chrome sessions are already closed or Something Wrong Happened!")


        elif 'open stackoverflow' in query:
            # webbrowser.open("stackoverflow.com")
            webbrowser.get(chrome_path).open("stackoverflow.com")
            speak("stackoverflow.com has been opened Successfully!, Thank for Using me.")

            # open a text file
        elif 'open notepad' in query:

            # CReating a file and writing to the same
            filecreationtime= datetime.datetime.now().strftime("%H_%M_%S")
            f = open("C:\\Development\\notepadFileCreation\\NewFile_"+filecreationtime+".txt", 'w')
            print(filecreationtime)
            str = "This file has been Created by VirtualAssistanceBot"
            f.write(str)
            speak("Note Pad file has been created Successfully!, Make Sure to rename your before closing It.")
            f.close()
            os.system("C:\\Development\\notepadFileCreation\\NewFile_"+filecreationtime+".txt")

        elif 'command prompt' in query:

            os.system("start cmd")
            speak("Command Prompt has been opened Successfully!, Thank for Using me.")
        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open vs code' in query:
            codePath = "C:\\Development\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            speak("VS code IDE has been Opened Successfully, Happy Coding!, Thank for Using me.")

        elif 'send email' in query:
            try:
                speak("What do youu want me to write in the email?")
                content = takeCommand()
                to = "diatmsubhankar@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent successfully!")
            except Exception as e:
                print(e)
                speak("Sorry!! . I am not able to send this email")

        elif 'who are you' or 'created you' in query:

            speak("I am "+botname+ " , developed by Subhankar Roy!!, I am here to help you!!")

        elif 'about yourself' in query:

            speak("I am "+botname+ " , developed by Subhankar Roy!!, I am here to help you!!")

        elif 'your future plans' in query:

            speak("I have been developed by Subhankar Roy!!, His plan is to use me for Intact Automation initiatives")

        elif '' or 'blank' in query:

            speak("Not received any inputs from you, terminating!")
  # Add new cases below
  #Then add new code here
  # This a new coment from another branch old dell lapy





