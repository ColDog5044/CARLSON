import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
import pywhatkit
import os
import yfinance as yf
import pyjokes


# listen to microphone and return the audio as text using google
def transform():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.8
        said = r.listen(source)
        try:
            print("I am listening")
            query = r.recognize_google(said, language="en")
            return query
        except sr.UnknownValueError:
            print("Sorry, I did not understand")
            return "I am waiting"
        except sr.RequestError:
            print("Sorry, the service is down")
            return "I am waiting"
        except:
            return "I am waiting"

# Speak Message
def speaking(message):
    engine = pyttsx3.init()
    id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-AU_JAMES_11.0"
    engine.setProperty("voice",id)
    engine.say(message)
    engine.runAndWait()


# Return the weekday name
def query_day():
    day = datetime.date.today()
    weekday = day.weekday()
    mapping = {
        0:"Monday",1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday",5:"Saturday",6:"Sunday"
    }
    try:
        speaking(f"Today is {mapping[weekday]}.")
    except:
        pass

# Returns the time
def query_time():
    time = datetime.datetime.now().strftime("%I:%M:%S")
    speaking(f"The current time is {time[0:2]} {time[3:5]}")

# Welcome Message
def welcome():
    query_day()
    query_time()
    speaking('''CARLSON is at your service sir.''')

def main():
    welcome()
    start = True
    while(start):
        query = transform().lower()

        if "open youtube" in query:
            speaking("opening youtube")
            webbrowser.open("https://youtube.com")
            continue

        elif "start chrome" in query:
            speaking("starting chrome")
            webbrowser.open("https://google.com")
            continue

        elif "disengage the studio" in query:
            speaking("disengaging the studio")
            break

        elif "search wikipedia" in query:
            speaking("On it sir")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query,sentences=2)
            speaking("Found on wikipedia.")
            speaking (result)

        elif "your name" in query:
            speaking("I am CARLSON, Computer Automated Robotic Listening Software Operations Navigation. How can I be of service sir?")
            continue

        elif "search web" in query:
            pywhatkit.search(query)
            speaking("This is what I found for you sir")
            continue

        elif "play" in query:
            speaking(f"playing {query}")
            pywhatkit.playonyt(query)
            continue

        elif "joke" in query:
            speaking(pyjokes.get_joke())
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
                speaking(f"found it sir, the price for {search} is {currentprice} dollars")
            except:
                speaking(f"Sorry sir, I found no data for {search}")
            continue

main()
