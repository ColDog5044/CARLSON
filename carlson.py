import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
import pywhatkit
import os
import yfinance as yf
import pyjokes

# Voice Setup
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",200)

# Speak Message
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def welcome():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning,")
    elif hour >=12 and hour <18:
        speak("Good Afternoon,")
    else:
        speak("Good Evening,")
    speak('''CARLSON is at your service sir.''')





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


# Return the weekday name
def query_day():
    day = datetime.date.today()
    weekday = day.weekday()
    mapping = {
        0:"Monday",1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday",5:"Saturday",6:"Sunday"
    }
    try:
        speak(f"Today is {mapping[weekday]}.")
    except:
        pass

# Returns the time
def query_time():
    time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(f"The current time is {time[0:2]} {time[3:5]}")


def main():
    welcome()
    start = True
    while(start):
        query = takeCommand().lower()

        if "open youtube" in query:
            speak("opening youtube")
            webbrowser.open("https://youtube.com")
            continue

        elif "start chrome" in query:
            speak("starting chrome")
            webbrowser.open("https://google.com")
            continue

        elif "disengage the studio" in query:
            speak("disengaging the studio")
            break

        elif "search wikipedia" in query:
            speak("On it sir")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query,sentences=2)
            speak("Found on wikipedia.")
            speak (result)

        elif "your name" in query:
            speak("I am CARLSON, Computer Automated Robotic Listening Software Operations Navigation. How can I be of service sir?")
            continue

        elif "search web" in query:
            pywhatkit.search(query)
            speak("This is what I found for you sir")
            continue

        elif "play" in query:
            speak(f"playing {query}")
            pywhatkit.playonyt(query)
            continue

        elif "joke" in query:
            speak(pyjokes.get_joke())
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
                speak(f"found it sir, the price for {search} is {currentprice} dollars")
            except:
                speak(f"Sorry sir, I found no data for {search}")
            continue

main()
