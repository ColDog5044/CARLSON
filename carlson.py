# Imported Libraries
import imp
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
import pywhatkit
import os
import yfinance as yf
import pyjokes
import speedtest
import pyautogui
from functions.media import volumeup, volumedown, volumemute, playpause, nexttrack, previoustrack
from functions.programs import startNotepad, startCalc, startCMD, startPWSH
from functions.utils import responses

# Voice Setup
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",180)

# Speak Message
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# listen to microphone and return the audio as text using google
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding...")
        query = r.recognize_google(audio,language="en-us")
        print(f"You Said: {query}\n")
    except Exception as e:
        print ("Say that again")
        return "None"
    return query

# Main Function
def main():
    while True:
        query = takeCommand().lower()
        if "carlson" in query and "wake up" in query:
            welcome()

        while True:
            query = takeCommand().lower()
            if "carlson" in query and "sleep" in query:
                speak("Ok sir, you can call me anytime.")
                break
            
            ########## CARLSON INTERACTION ##########

            elif "what is your name" in query:
                speak("I am CARLSON, Computer Automated Robotic Listening Software Operations Navigation. How can I be of service sir?")
                continue

            elif "who created you" in query:
                speak("I was created by Collin Laney, on October Thirteenth, Twenty Twenty-Two.")
                continue

            elif "what is your birth day" in query:
                speak("October Thirteenth, Twenty Twenty-Two.")
                continue

            elif "hello" in query:
                speak("Hello sir, how are you?")
                continue

            elif "i am" in query or "i'm" in query:
                speak("That's great sir.")
                continue
            
            elif "how are you" in query:
                speak("Perfect sir.")
                continue
            
            elif "thank you" in query:
                speak("You are welcome sir.")
                continue

            elif "joke" in query:
                speak(pyjokes.get_joke())
                continue

            ########## MEDIA CONTROLS ##########

            elif "resume" in query or "pause" in query:
                playpause()
                continue

            elif "mute" in query:
                volumemute
                continue

            elif "volume up" in query:
                volumeup()
                continue

            elif "volume down" in query:
                volumedown()
                continue
            
            elif "skip" in query:
                nexttrack()
                continue

            elif "previous" in query:
                previoustrack()
                continue

            ########## CARLSON REQUESTS ##########

            elif "test internet speed" in query:
                internet = speedtest.Speedtest()
                downloadSpeed = internet.download()/1048576     # Megabyte = 1024*1024 Bytes
                uploadSpeed   = internet.upload()/1048576
                speak(f"Internet Download Speed is {downloadSpeed} Megabytes.")
                speak(f"Internet Upload Speed is {uploadSpeed} Megabytes.")
                
            elif "wikipedia" in query:
                speak("On it sir.")
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query,sentences=2)
                speak("Here is what I found on Wikipedia.")
                speak(result)
                continue

            elif "search" in query:
                query = query.replace("search", "")
                pywhatkit.search(query)
                speak("This is what I found for you sir.")
                continue

            elif "open google" in query:
                speak("On it sir.")
                webbrowser.open("https://google.com")
                continue

            elif "stock price" in query:
                search = query.split("of")[-1].strip()
                lookup = {"apple":"AAPL",
                          "amazon":"AMZN",
                          "google":"GOOGL"}
                try:
                    stock = lookup[search]
                    stock = yf.Ticker(stock)
                    currentprice = stock.info["regularMarketPrice"]
                    speak(f"Found it sir, the price for {search} is {currentprice} dollars.")
                except:
                    speak(f"Sorry sir, I found no data for {search}.")
                continue

            elif "disengage glass box" in query:
                speak("Are you sure you want to shutdown?")
                shutdown = input("Do you wish to shutdown your computer? Yes/No")
                if shutdown == "yes":
                    os.system("shutdown /s /t 1")

                elif shutdown == "no":
                    break
            
########## FUNCTIONS ##########

# Welcome Greeting
def welcome():
    hour = datetime.now().hour
    if hour>=0 and hour<12:
        speak("Good Morning,")
    elif hour >=12 and hour <18:
        speak("Good Afternoon,")
    else:
        speak("Good Evening,")
    speak('''CARLSON is at your service sir.''')

# Return the weekday name
def weekday():
    day = datetime.date.today()
    weekday = day.weekday()
    mapping = {
        0:"Monday",1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday",5:"Saturday",6:"Sunday"
    }
    try:
        speak(f"Today is {mapping[weekday]}.")
    except:
        pass

main()
