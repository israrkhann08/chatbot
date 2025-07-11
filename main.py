import datetime
import os
import sys
import time
import webbrowser
import pyautogui
import pyttsx3
import speech_recognition as sr

import json
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import random
import numpy as np

with open("intents.json") as file:
    data = json.load(file)

model = load_model("chat_model.h5")

with open("tokenizer.pkl", "rb") as f:
    tokenizer=pickle.load(f)

with open("label_encoder.pkl", "rb") as encoder_file:
    label_encoder=pickle.load(encoder_file)


def initialize_engine():
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 50)  # Corrected line
    volume = engine.getProperty('volume')
    engine.setProperty('volume', volume + 0.25)
    return engine

def speak(text):
    engine = initialize_engine()
    engine.say(text)
    engine.runAndWait()

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        print("Listening......", end="", flush=True)
        r.pause_threshold=1.0 # properties for the recognizer
        r.phrase_threshold=0.3
        r.sample_rate = 48000
        r.dynamic_energy_threshold = True
        r.operation_timeout= 5
        r.non_speaking_duration= 0.5
        r.dynamic_energy_adjustment = 2
        r.energy_threshold = 4000
        r.phrase_time_limit = 10
        # print(sr.Microphone.list_microphones_names())
        audio = r.listen(source)
    try:
        print("\r", end="", flush=True)
        print("Recognizing.....", end="", flush=True)
        query = r.recognize_google(audio, language= 'en-in')
        print("\r", end="", flush=True)
        print(f"User Said: {query}\n")
    except Exception as e:
        print('Say, that again please')
        return "None"
    return query

def cal_day():
    day = datetime.datetime.today().weekday() + 1
    day_dist={
       1: "Monday",
       2: "Tuesday",
       3: "Wednesday",
       4: "Thursday",
       5: "Friday",
       6: "Saturday",
       7: "Sunday"
    }
    if day in day_dist.keys():
        day_of_week =  day_dist[day]
        print(day_of_week)
    return day_of_week    

def wishme():
    hour =int( datetime.datetime.now().hour)   # control + .  import libraray
    t = time.strftime("%I:%M:%p")
    day = cal_day()

    if(hour >= 0) and (hour <= 12) and ('AM' in t):
        speak(f"Good Morning Sir, it's {day} and the time is {t}")
    elif(hour >= 12) and (hour <= 16) and ('PM' in t):    
        speak(f"Good afternoon Sir, it's {day} and the time is {t}")
    else:
        speak(f"Good evening Sir, it's {day} and the time is {t}")

def social_media(command):
    if 'facebook' in command:
        speak('Opening your facebook')
        webbrowser.open('https://www.facebook.com/')
    elif 'whatsapp' in command:
        speak('Opening your Whatsapp')
        webbrowser.open('https://web.whatsapp.com/')    
    elif 'discord' in command:
        speak('Opening your discord server')
        webbrowser.open('https://www.discord.com/')    
    elif 'instagram' in command:
        speak('Opening your instagram')
        webbrowser.open('https://www.instagram.com/')  
    else:
        speak('No result found')      

def schedule():
    day = cal_day().lower()
    speak("Today your scheduling time table is")
    week={
        "monday": "from 9:00 am  to 9:50 am you have algorith class, 11:00 am tp 12:00 pm ou have a DSA class",
        "tuesday": "from 9:00 am  to 9:50 am you have CCNA class, 11:00 am tp 12:00 pm ou have a web development class",
        "wednesday": "from 9:00 am  to 9:50 am you have c++ class, 11:00 am tp 12:00 pm ou have a DSA class",
        "thursday": "from 9:00 am  to 9:50 am you have algorith class, 11:00 am tp 12:00 pm ou have a DSA class",
        "friday": "from 9:00 am  to 9:50 am you have algorith class, 11:00 am tp 12:00 pm ou have a DSA class",
        "saturday": "from 9:00 am  to 9:50 am you have algorith class, 11:00 am tp 12:00 pm ou have a DSA class",
        "sunday": "from 9:00 am  to 9:50 am you have algorith class, 11:00 am tp 12:00 pm ou have a DSA class"
    }
    if day in week.keys():
        speak(week[day])

def openApp(command):
    if "calculator" in command:
        speak("Calculator is open")
        os.startfile('C:\\windows\\system32\\calc.exe')          # control + .
    elif "notepad" in command:
        speak("Notepad is open")
        os.startfile('C:\\windows\\system32\\notepad.exe')         
    elif "paint" in command:
        speak("Paint is open")
        os.startfile('C:\\windows\\system32\\mspaint.exe')    
   
def closeApp(command):
    if "calculator" in command:
        speak("Calculator is close")
        os.system('taskkill /f /im calc.exe')         
    elif "notepad" in command:
        speak("Notepad is close")
        os.system('taskkill /f /im notepad.exe')         
    elif "paint" in command:
        speak("Paint is close")
        os.system('taskkill /f /im mspaint.exe')  

if __name__ =="__main__":
    while True:
        # wishme()
        # query = command().lower()
        query = input("Enter your command ->")
        # add social media feature:
        if('facebook' in query) or ('discord' in query) or ('whatsapp' in query) or ('instagram' in query):
            social_media(query)
        # add schedule feature in 
        elif("Schedule Time table" in query) or ("schedule" in query):
            schedule() 
        # volume up feature add    
        elif("volume up" in query) or ("increase volume" in query):
            pyautogui.press("volumeup")   # package install pyautogui
            speak("Volume increase")  
        elif("volume down" in query) or ("decrease volume" in query):
            pyautogui.press("volumedown")
            speak("Volume decrease")  
        elif("volume mute" in query) or ("mute the sound " in query):
            pyautogui.press("volumemute")
            speak("Volume muted")  
        # opening appication feature:
        elif("open calculator" in query) or ("open notepad" in query) or ("open paint" in query):
            openApp(query)
         # closing the application
        elif("close calculator" in query) or ("close notepad" in query) or ("close paint" in query):
            closeApp(query)
        #implement the model_test in this main.py
        elif("what" in query) or ("who" in query) or ("how" in query) or ("hi" in query) or ("thanks" in query) or ("hello" in query):
            padded_sequences = pad_sequences(tokenizer.texts_to_sequences([query]), maxlen=20, truncating='post')
            result = model.predict(padded_sequences)
            tag = label_encoder.inverse_transform([np.argmax(result)])

            for i in data['intents']:
                if i['tag'] == tag:
                    speak(np.random.choice(i['responses']))


        elif "exit" in query:     # if it is exist inside my query so that they start the infinate loop bease it taking the command again and again      
            sys.exit()            # import control + .
       
# speak('hello israr How are you')