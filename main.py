import datetime
import time
import pyttsx3
import speech_recognition as sr

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

if __name__ =="__main__":
    while True:
        wishme()
        # query = command().lower()
        # query = input("Enter your command ->")
        # print(query)
# speak('hello israr How are you')