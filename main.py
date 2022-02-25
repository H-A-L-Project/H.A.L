import re
import speech_recognition as sr #convert speech to text
import datetime #for fetching date and time
import wikipedia #Search Wikipedia for data
import webbrowser #Search Web
from gtts import gTTS # google text to speech
import os # to save/open files 
from selenium import webdriver # to control browser operations
import time
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
from pygame import mixer #Play sound
import pygame
from mutagen.mp3 import MP3 #Read length of audio file
from art import * #Make H.A.L Font
import random
import requests
from dotenv import load_dotenv #To Get Access To Config File
import asyncio
from bs4 import BeautifulSoup as bs
from covid import Covid #To get coivd data
import base64 #Encode text in base64
import platform #To Find OS
import urllib.request #To find version number
import calendar #To show calendar
import datetime

load_dotenv()
os_name = platform.system()

def jokes():
    response = ["I'm afraid for the calendar. Its days are numbered",
                "My friend said I should do lunges to stay in shape. That would be a big step forward",
                "Why do fathers take an extra pair of socks when they go golfing?" "In case they get a hole in one",
                "Singing in the shower is fun until you get soap in your mouth. Then it's a soap opera.",
                "What do a tick and the Eiffel Tower have in common?" "They're both Paris sites.",
                "What do you call a fish wearing a bowtie?" "Sofishticated.",
                "How do you follow Will Smith in the snow?" "You follow the fresh prints.",
                "If April showers bring May flowers, what do May flowers bring?" "Pilgrims.",
                "I thought the dryer was shrinking my clothes. Turns out it was the refrigerator all along.",
                "What do you call a factory that makes okay products?" "A satisfactory.",
                "Dear Math, grow up and solve your own problems.",
                "What did the janitor say when he jumped out of the closet? Supplies!",
                "Have you heard about the chocolate record player? It sounds pretty sweet.",
                "What did the ocean say to the beach? Nothing, it just waved.",
                "Why do seagulls fly over the ocean? Because if they flew over the bay, we'd call them bagels.",
                "I only know 25 letters of the alphabet. I don't know y.",
                "How does the moon cut his hair? Eclipse it.",
                "What did one wall say to the other? I'll meet you at the corner.",
                "What did the zero say to the eight? That belt looks good on you.",
                "A skeleton walks into a bar and says, Hey, bartender. I'll have one beer and a mop.",
                "Where do fruits go on vacation? Pear-is!",
                "I asked my dog what's two minus two. He said nothing.",
                "What did Baby Corn say to Mama Corn? Where's Pop Corn?",
                "What's the best thing about Switzerland? I don't know, but the flag is a big plus.",
                "What does a sprinter eat before a race?" "Nothing, they fast!",
                "Where do you learn to make a banana split?" "Sundae school.",
                "What has more letters than the alphabet?" "The post office!",
                "What do you call a poor Santa Claus? St. Nickel-less.",
                "I got carded at a liquor store, and my Blockbuster card accidentally fell out. The cashier said never mind.",
                "Where do boats go when they're sick? To the boat doc.",
                "I don't trust those trees. They seem kind of shady.",
                "My wife is really mad at the fact that I have no sense of direction. So I packed up my stuff and right!",
                "How do you get a squirrel to like you? Act like a nut.",
                "Why don't eggs tell jokes? They'd crack each other up.",
                "I don't trust stairs. They're always up to something.",
                "What do you call someone with no body and no nose? Nobody knows.",
                "Did you hear the rumor about butter? Well, I'm not going to spread it!",
                "Why couldn't the bicycle stand up by itself? It was two tired.",
                "What did one hat say to the other?" "Stay here! I'm going on ahead.",
                "Why did Billy get fired from the banana factory? He kept throwing away the bent ones.",
                "Dad, can you put my shoes on? No, I don't think they'll fit me.",
                "Why can't a nose be 12 inches long? Because then it would be a foot.",
                "What does a lemon say when it answers the phone?" "Yellow!",
                "This graveyard looks overcrowded. People must be dying to get in.",
                "What kind of car does an egg drive?" "A yolkswagen.",
                "Dad, can you put the cat out?" "I didn't know it was on fire.",
                "How do you make 7 even?" "Take away the s.",
                "How does a taco say grace?" "Lettuce pray.",
                "What time did the man go to the dentist? Tooth hurt-y.",
                "Why didn't the skeleton climb the mountain?" "It didn't have the guts.",
                "What do you call it when a snowman throws a tantrum?" "A meltdown.",
                "How many tickles does it take to make an octopus laugh? Ten tickles.",
                "I have a joke about chemistry, but I don't think it will get a reaction.",
                "What concert costs just 45 cents? 50 Cent featuring Nickelback!",
                "What does a bee use to brush its hair?" "A honeycomb!",
                "How do you make a tissue dance? You put a little boogie in it.",
                "Why did the math book look so sad? Because of all of its problems!",
                "What do you call cheese that isn't yours? Nacho cheese.",
                "My dad told me a joke about boxing. I guess I missed the punch line.",
                "What kind of shoes do ninjas wear? Sneakers!",
                "How does a penguin build its house? Igloos it together."
                ][
        random.randrange(61)]
    return response

def quote():
    response = ["The greatest glory in living lies not in never falling, but in rising every time we fall. -Nelson Mandela",
    "The way to get started is to quit talking and begin doing. -Walt Disney",
    "Your time is limited, so don't waste it living someone else's life. Don't be trapped by dogma which is living with the results of other people's thinking. -Steve Jobs",
    "If life were predictable it would cease to be life, and be without flavor. -Eleanor Roosevelt",
    "If you look at what you have in life, you'll always have more. If you look at what you don't have in life, you'll never have enough. -Oprah Winfrey",
    "If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success. -James Cameron",
    "Life is what happens when you're busy making other plans. -John Lennon",
    "Spread love everywhere you go. Let no one ever come to you without leaving happier. -Mother Teresa",
    "When you reach the end of your rope, tie a knot in it and hang on. -Franklin D. Roosevelt",
    "Always remember that you are absolutely unique. Just like everyone else. -Margaret Mead",
    "Don't judge each day by the harvest you reap but by the seeds that you plant. -Robert Louis Stevenson",
    "The future belongs to those who believe in the beauty of their dreams. -Eleanor Roosevelt",
    "Tell me and I forget. Teach me and I remember. Involve me and I learn. -Benjamin Franklin",
    "Whoever is happy will make others happy too. -Anne Frank",
    "Do not go where the path may lead, go instead where there is no path and leave a trail. -Ralph Waldo Emerson",
    "You will face many defeats in life, but never let yourself be defeated. -Maya Angelou",
    "The greatest glory in living lies not in never falling, but in rising every time we fall. -Nelson Mandela",
    "In the end, it's not the years in your life that count. It's the life in your years. -Abraham Lincoln",
    "Never let the fear of striking out keep you from playing the game. -Babe Ruth",
    "Many of life's failures are people who did not realize how close they were to success when they gave up. -Thomas A. Edison",
    "You have brains in your head. You have feet in your shoes. You can steer yourself any direction you choose. -Dr. Seuss",
    "Keep smiling, because life is a beautiful thing and there's so much to smile about. -Marilyn Monroe",
    "Life is a long lesson in humility. -James M. Barrie",
    "In three words I can sum up everything I've learned about life: it goes on. -Robert Frost",
    "Love the life you live. Live the life you love. -Bob Marley",
    "Life is either a daring adventure or nothing at all. -Helen Keller",
    "You have brains in your head. You have feet in your shoes. You can steer yourself any direction you choose. -Dr. Seuss"
    ][
        random.randrange(27)]
    return response    

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
# US english
LANGUAGE = "en-US,en;q=0.5"

def get_weather_data(url):
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    html = session.get(url)
    # create a new soup
    soup = bs(html.text, "html.parser")
    # store all results on this dictionary
    result = {}
    # extract region
    result['region'] = soup.find("div", attrs={"id": "wob_loc"}).text
    # extract temperature now
    result['temp_now'] = soup.find("span", attrs={"id": "wob_tm"}).text
    # get the day and hour now
    result['dayhour'] = soup.find("div", attrs={"id": "wob_dts"}).text
    # get the actual weather
    result['weather_now'] = soup.find("span", attrs={"id": "wob_dc"}).text
    # get the precipitation
    result['precipitation'] = soup.find("span", attrs={"id": "wob_pp"}).text
    # get the % of humidity
    result['humidity'] = soup.find("span", attrs={"id": "wob_hm"}).text
    # extract the wind
    result['wind'] = soup.find("span", attrs={"id": "wob_ws"}).text
    # get next few days' weather
    next_days = []
    days = soup.find("div", attrs={"id": "wob_dp"})
    for day in days.findAll("div", attrs={"class": "wob_df"}):
        # extract the name of the day
        day_name = day.findAll("div")[0].attrs['aria-label']
        # get weather status for that day
        weather = day.find("img").attrs["alt"]
        temp = day.findAll("span", {"class": "wob_t"})
        # maximum temparature in Celsius, use temp[1].text if you want fahrenheit
        max_temp = temp[0].text
        # minimum temparature in Celsius, use temp[3].text if you want fahrenheit
        min_temp = temp[2].text
        next_days.append({"name": day_name, "weather": weather, "max_temp": max_temp, "min_temp": min_temp})
    # append to result
    result['next_days'] = next_days
    return result
    

def talk():
    input=sr.Recognizer()
    with sr.Microphone() as source:
        audio=input.listen(source)
        data=""
        try:
            data=input.recognize_google(audio)
            print("Your question is: " + data)
            
        except sr.UnknownValueError:
            respond("Sorry I did not hear your question, Please repeat it again.")
    return data

def respond(output):
    num=0
    print(output)
    num += 1
    response=gTTS(text=output, lang='en')
    file = str(num)+".mp3"
    response.save(file)
    mixer.init()
#Load audio file
    mixer.music.load(file)
    #Set preferred volume
    mixer.music.set_volume(1)

    #Play the audio file
    mixer.music.play()
    song = MP3(file)
    songLength = song.info.length
    time.sleep(songLength)
    mixer.music.stop()
    pygame.quit()
    os.remove(file)

def countdown(h, m, s):
 
    # Calculate the total number of seconds
    total_seconds = h * 3600 + m * 60 + s
 
    # While loop that checks if total_seconds reaches zero
    # If not zero, decrement total time by one second
    while total_seconds > 0:
        # Timer represents time left on countdown
        timer = datetime.timedelta(seconds = total_seconds)      
        # Prints the time left on the timer
        print(timer, end="\r")
        # Delays the program one second
        time.sleep(1)
        # Reduces total time by one second
        total_seconds -= 1
    mixer.init()
    file = "sounds/timer.mp3"
    mixer.music.load(file)
    mixer.music.set_volume(1)
    mixer.music.play()
    song = MP3(file)
    songLength = song.info.length
    time.sleep(songLength)
    respond("Your Timer Is At Zero")

def main():
    tprint("H.A.L")
    print("HELPFUL ARTIFICIAL LISTENER")
    print("Current Version: 2.7.5")
    print("")
    time.sleep(1)
    respond("Hello, I am hal your personal desktop assistant")
        
    while(1):
        respond("How can I help you?")
        print("Listening...")
        text=talk().lower()
        
        if text==0:
            continue

        if 'search amazon' in text:
            text = text.replace("search amazon", "")
            webbrowser.open(f"https://www.amazon.com/s?k={text}")
            respond(f"Searching amazon for {text}")
            
        elif "stop" in str(text) or "exit" in str(text) or "bye" in str(text) or "cancel" in str(text):
            respond("Goodbye")
            mixer.init()
            file = "sounds/exit.mp3"
            mixer.music.load(file)
            mixer.music.set_volume(1)
            mixer.music.play()
            song = MP3(file)
            songLength = song.info.length
            time.sleep(songLength)
            break

        elif text ==  "encode message":
            sample_string = input("Enter Message To Encode: ")
            sample_string_bytes = sample_string.encode("ascii")
            base64_bytes = base64.b64encode(sample_string_bytes)
            base64_string = base64_bytes.decode("ascii")
            print(base64_string)
            respond("Message Is Encoded")

        elif text ==  "decode message":
            base64_string = input("Enter string to decode: ")
            base64_bytes = base64_string.encode("ascii")  
            sample_string_bytes = base64.b64decode(base64_bytes)
            message = sample_string_bytes.decode("ascii")
            print(message)
            respond("Message Is Encoded")       

        elif 'weather' in text:
            token = os.environ.get("cellOrFar")
            if token == "F" or "f":
                URL = "https://www.google.com/search?lr=lang_en&ie=UTF-8&q=weather"
                import argparse
                parser = argparse.ArgumentParser()
                parser.add_argument("region", nargs="?",default="")
                # parse arguments
                args = parser.parse_args()
                region = args.region
                if region:
                    region = region.replace(" ", "+")
                    URL += f"+{region}"
                # get data
                data = get_weather_data(URL)
                # print data
                print("Weather for:", data["region"])
                print("Now:", data["dayhour"])
                print(f"Temperature now: {data['temp_now']}°F")
                print("Description:", data['weather_now'])
                print("Precipitation:", data["precipitation"])
                print("Humidity:", data["humidity"])
                print("Wind:", data["wind"])
                print("Next days:")
                for dayweather in data["next_days"]:
                    print("="*40, dayweather["name"], "="*40)
                    print("Description:", dayweather["weather"])
                    print(f"Max temperature: {dayweather['max_temp']}°F")
                    print(f"Min temperature: {dayweather['min_temp']}°F") 

            else:
                URL = "https://www.google.com/search?lr=lang_en&ie=UTF-8&q=weather"
                import argparse
                parser = argparse.ArgumentParser()
                parser.add_argument("region", nargs="?",default="")
                # parse arguments
                args = parser.parse_args()
                region = args.region
                if region:
                    region = region.replace(" ", "+")
                    URL += f"+{region}"
                # get data
                data = get_weather_data(URL)
                # print data
                print("Weather for:", data["region"])
                print("Now:", data["dayhour"])
                print(f"Temperature now: {data['temp_now']}°C")
                print("Description:", data['weather_now'])
                print("Precipitation:", data["precipitation"])
                print("Humidity:", data["humidity"])
                print("Wind:", data["wind"])
                print("Next days:")
                for dayweather in data["next_days"]:
                    print("="*40, dayweather["name"], "="*40)
                    print("Description:", dayweather["weather"])
                    print(f"Max temperature: {dayweather['max_temp']}°C")
                    print(f"Min temperature: {dayweather['min_temp']}°C") 
                
        if 'wikipedia' in text:
            try:     
                text = text.replace("wikipedia","" )
                respond(f'Searching Wikipedia For {text}')
                results = wikipedia.summary(text, sentences=4)
                respond("According to Wikipedia")
                respond(results)

            except:
                respond("Sorry, There was an error")

        elif 'say' in text:
            text =text.replace("say", "")
            respond(text)

        elif 'set a timer' in text:
            h = input("Enter the time in hours: ")
            m = input("Enter the time in minutes: ")
            s = input("Enter the time in seconds: ")
            countdown(int(h), int(m), int(s))           

        elif 'time' in text:
            token = os.environ.get("24hourclock")

            if token == 'False':
                strTime=datetime.datetime.now().strftime("%I:%M:%S %p")
                respond(f"the time is {strTime}")

            else:
                strTime=datetime.datetime.now().strftime("%H:%M:%S")
                respond(f"the time is {strTime}")

        elif 'bestbuy' in text:
            text = text.replace("bestbuy", "")
            webbrowser.open(f"https://www.bestbuy.com/site/searchpage.jsp?st={text}")
        
        elif 'search' in text:
            token = os.environ.get("UseGoogle")
            if token == 'True':
                text = text.replace("search","")
                webbrowser.open(f'https://www.google.com/search?q={text}')
                respond(f"Searching Google For {text}")
            
            else:
                text = text.replace("search","")
                webbrowser.open(f'https://duckduckgo.com/?q={text}')
                respond(f"Searching DuckDuckGo For {text}")
            
        elif 'google' in text:
            webbrowser.open('https://google.com')
            respond("Google is open")
            
        elif text == 'open youtube':
            webbrowser.open('https://youtube.com')
            respond("youtube is open")
        
        elif 'amazon' in text:
            webbrowser.open("https://amazon.com")
            respond('amazon is open')

        elif 'visual studio' in text:
            os.system('code')
            respond('Visual Studio is open')
        
        elif ' open music' in text:
            token = os.environ.get("UseSpotify")
            if token == 'True':
                webbrowser.open("https://open.spotify.com/")
                respond("Music is open")
            else:
                webbrowser.open('https://music.amazon.com/?')
                respond('Music is open')

        elif 'hbo' in text:
            webbrowser.open('https://play.hbomax.com/page/urn:hbo:page:home')
            respond('HBO Is Open')
        
        elif 'pause' in text:
            respond('I Am Now Paused')
            input("Enter To Continue: ")

        elif 'joke' in text:
            respond(jokes())

        elif 'quote' in text:
            respond(quote())

        elif 'netflix' in text:
            webbrowser.open("https://www.netflix.com/browse")
            respond("Netflix Is Open")

        elif 'covid test' in text:
            webbrowser.open("https://www.cvs.com/minuteclinic/covid-19-testing")
            respond("Remember to stay safe")

        elif 'command prompt' in text:
            os.system('start cmd')
            respond("cmd is open")

        elif 'python' in text:
            os.system('start python')
            respond("python is open")

        elif 'news' in text:
            main_url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=00cb4bc87f5241d3bcff3ff33e28db27"
            news=requests.get(main_url).json()
            article = news['articles']

            news_article = []
            for arti in article:
                news_article.append(arti['title'])
            
            respond('Here Are The First 10 Major News Head Lines')

            for i in range(10):
                print(i+1, news_article[i])

        elif 'good morning' in text:
            respond('Good Morning')

        elif 'hello hal' in text:
            respond('Hello How are you')

        elif 'recipe' in text:
            text = text.replace("recipe","")
            webbrowser.open(f"https://www.allrecipes.com/search/results/?search={text}")
            respond(f'Here Is a recipe for {text}')

        elif 'play' in text:
            token = os.environ.get("UseSpotify")
            if token == "True":
                text = text.replace("play", "")
                webbrowser.open(f"https://open.spotify.com/search/{text}")
                respond(f"Searching Spotify For {text}")

            else:
                text = text.replace("play", "")
                webbrowser.open(f"https://music.amazon.com/search/{text}")
                respond(f"Searching Amazon Music For {text}")

        elif 'sport' in text:
            webbrowser.open("https://www.espn.com/")


        if text == "update":
            respond("Updating To Latest Version")
            webbrowser.open("https://github.com//AstroBolo/H.A.L/archive/refs/heads/main.zip")

        elif 'wordle' in text:
            webbrowser.open("https://www.nytimes.com/games/wordle/")
            respond("Wordle is now open")

        elif 'random number' in text:
            respond(f'your random number is {random.randint(0,1000)}')


if __name__=='__main__':
    token = os.environ.get("IntroMusic")
    if token == "True":
        mixer.init()
        file = "sounds/start.mp3"
        mixer.music.load(file)
        mixer.music.set_volume(1)
        mixer.music.play()
        song = MP3(file)
        songLength = song.info.length
        time.sleep(songLength)
        main()

    else:
        main()