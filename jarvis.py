import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

import pyttsx3
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def salutationMe():
    '''
    This function wishes me Good Morning or Afternoon or evening
    according to time.
    '''

    hrs=int(datetime.datetime.now().hour)
    if hrs>=0 and hrs<12:
        speak("Good Morning Dear Sir!!")
    elif hrs>=12 and hrs<=18:
        speak("Good Afternoon Dear Sir!!")
    else:
        speak("Good Evening Dear Sir!!")
    speak("I am your assistant. Kindly tell me, How may I help you?")

def takeOrder():
    '''
    This function takes my command/order as an argument.

    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        order= r.recognize_google(audio, language='en-in')
        print(f"Boss said : {order}\n")
    except Exception as e:
        print("Sir!! Please speak again")
        return "None"
    return order

if __name__ == '__main__':
    salutationMe()
    while True:
        order=takeOrder().lower()
        if 'wikipedia' in order:
            speak("Searching wikipedia...")
            order=order.replace("wikipedia"," ")
            results=wikipedia.summary(order,sentences=1)
            speak("According to wikipedia..")
            print(results)
            speak(results)
        elif "open facebook" in order:
            webbrowser.open("facebook.com")
        elif "open youtube" in order:
            webbrowser.open("youtube.com")
        elif "open google" in order:
            webbrowser.open("google.com")
        elif "play music for me" in order:
            music_dir="C:\\Users\\HP\\Downloads\\mixkit-liquid-poured-in-a-jar-with-ice-125.wav"
            os.startfile(music_dir)
        elif "tell me time please" in order:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir now time is {strtime}")
        #elif "" in order:
            codepath="C:\\Users\\HP\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"
            os.startfile(codepath)