
from http import server
import smtplib
import os
from tkinter import EXCEPTION
from flask import request
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import datetime
import cv2
import random
from requests import get
import pywhatkit as kit
import sys
import pyjokes
import pyautogui
import requests
import time

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

#Text to speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=6 and hour<12:
        speak("Good morning")

    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:
        speak("Good evening")
    speak("I am  Prototype 1,how may i help you ")

#To convert voice into text
def takeCommand():      
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening..")
        r.pause_threshold=1
        #r.energy_threshold=200
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query= r.recognize_google(audio, language='en-in')
        print(f"User said {query}\n")
    except Exception as e:
        #print(e)
        print("Say that again please")
        speak("Say that again please")
        return "None"
    return query

def  sendEmail(to, content):
    
    server=smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('zakkiwork732.gmail.com','z@kkiworks786')
    server.sendmail('zakkiwork732.gmail.com',to,content)
    server.close()   

def news():
    #3801ee1289054d0b931574de41a92cd0
    main_url='http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=3801ee1289054d0b931574de41a92cd0'
    main_page=requests.get(main_url).json() 
    #print(main_page)
    articles=main_page["articles"]
    #print(articles)
    head=[]
    day=["first","second","third","fourth","fifth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        #print(f"Today's {day[i]} nes is: {head[i]}")
        speak(f"Today's {day[i]} news is: {head[i]}")
if __name__=="__main__":
    wishMe()
    while True:
        query=takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia..')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=3)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            speak("Sir,what should I search on google")
            gs=takeCommand().lower()
            webbrowser.open(f"{gs}")
       
        elif 'send message' in query:
            kit.sendwhatmsg("+918451978821","This message is send bt Prototype 1",12,42)

        elif 'play song on youtube' in query:
            kit.playonyt("Excuses Ap Dhillon")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
       
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
       
        elif 'open whatsapp ' in query:
            webbrowser.open("whatsapp.com")
       
        elif 'open javatpoint' in query:
            webbrowser.open("javatpoint.com")
        
        elif 'ip address' in query:
            ip=get('https://api.ipify.org').text
            speak(f"{ip} is your ip Address")
            print(f"{ip} is your ip Address")

        elif 'open camera' in query:
            cap=cv2.VideoCapture(0)
            while True:
                ret, img=cap.read()
                cv2.imshow('webcam',img)
                k=cv2.waitKey(25)
                if k==10:
                    break
            cap.release()
            cv2.destroyAllWindows()


        elif 'tell me a joke' in query:
            joke=pyjokes.get_jokes()
            speak(joke)
            
        elif 'tell me news' in query:
            speak('please wait sir, fetching the latest news')
            news()

        elif 'switch window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            pyautogui.keyUp("alt")
            

        elif 'play music' in query:
            Music_dir='G:\\ASAD\\songs'
            songs=os.listdir(Music_dir)
            rd=random.choice(songs)
            #print(songs)
            os.startfile(os.path.join(Music_dir,rd))
        
        elif 'the time' in query or 'what time it is' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir ,the time is{strTime}")
            print(f"Sir ,the time is{strTime}")

        elif 'open vs code' in query:
            codePath="C:\\Users\\Admin\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
            os.startfile(codePath)

        elif 'open notepad' in query:
            codePath="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\notepad"
            os.startfile(codePath)

        elif 'close notepad' in query:
            speak("Okay sir,closing notepad")
            os.system("taskkill /f /im notepad.exe")
           
        elif 'set alarm' in query:
          alarm=int(datetime.datetime.now().hour)
          if alarm==22:
              music_dir='G:\\ASAD\\songs\\Kacha Badam'
              songs=os.listdir(music_dir)
              os.startfile(os.path.join(music_dir,songs[0]))  

        elif 'send email to' in query:
            try:
                speak("What should i say?")
                content="this is a test message "
                to="zakkiwork732@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")

            except Exception as e:
                print(e)
                speak("Sorry Sir im not able to send this Email currently")

        elif 'you can sleep' in query:
            speak("Thanks,have a good day")
            print("Thanks,have a good day")
            exit() 
        
        elif 'shutdown the system' in query:
            os.system("shutdown /s /t 5")

        
        elif 'restart the system' in query:
            os.system("shutdown /r /t 5")