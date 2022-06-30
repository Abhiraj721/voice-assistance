import numToWord
import pyttsx3
import datetime
import random
import pywhatkit
import wikipedia
import webbrowser
from googlesearch import search
import os
import pywhatkit as pk
import speech_recognition as sr
from word2number import w2n
from num2words import num2words
import pywhatkit as kit
import json
import requests



engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[6].id)


def asteroid():
    start="2022-02-17"
    end="2022-02-24"
    key="IPw6It7uhbUK1yPpTFYmK8RhLhLgdGiyAMN6p6gt"
    url=f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start}&end_date={end}&api_key=IPw6It7uhbUK1yPpTFYmK8RhLhLgdGiyAMN6p6gt"
    response=requests.get(url)
    raw=response.json()
    total_asteroid=(raw['element_count'])
    speak(f"total {total_asteroid} asteroid detected this week")
    speak(f"sir do you want data of all {total_asteroid} asteroid")
    r=sr.Recognizer()
    with sr.Microphone() as source:
        pause_threshold=1
        print("Listening......")
        audio6=r.listen(source)

        query7=r.recognize_google(audio6,language="en-in").lower()
    if "yes" in query7:    
        speak("collecting data")
        print(raw['near_earth_objects'])
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def game():
    speak("yes sir,I have bunch of games installed like rock paper scissors and tic tac toe")
    speak("which one you want to play")
    r=sr.Recognizer()
    with sr.Microphone() as source:
        pause_threshold=1
        print("Listening......")
        audio6=r.listen(source)

        query7=r.recognize_google(audio6,language="en-in").lower()
        print('Recognizing......')
        print(query7)
    if "rock" in query7:
        speak("ok lets play,its your turn sir")
        iinput="sdsd"
        while iinput!="quit":
            r=sr.Recognizer()
            with sr.Microphone() as source:
                pause_threshold=1
                print("Listening......")
                audio6=r.listen(source)
                iinput=r.recognize_google(audio6,language="en-in")

            houd=["rock","paper","scissors"]
            num=int(random.randint(0,2))
            computer_pick=houd[num]
            speak(computer_pick)
            if iinput=="rock"and computer_pick=="paper":
                speak("its me yes")
            elif iinput=="paper" and computer_pick=="rock":
                speak("you won sir!!")
            elif iinput=="rock" and computer_pick=="scissors":
                speak("you win sir!!")
            elif iinput=="paper" and computer_pick=="scissors":
                speak("yes i won!")
            elif iinput == "paper" and computer_pick == "rock":
                speak("yes i won")
            elif iinput=="scissors" and computer_pick=="rock":
                speak("finally its me yes")
            elif iinput=="scissors" and computer_pick=="paper":
                speak("you won sir!!")
            elif iinput=="scissors" and computer_pick=="rock":
                speak("yes i won!!")
            elif iinput=="scissors" and computer_pick=="paper":
                speak("you won sir!")

def nasa_apod():
    nasa_key="JabGrBrnbEFc2vkGu6h2aRi31Y1tWsQEqv9OWu6s"
    url="https://api.nasa.gov/planetary/apod"
    params={'api_key':nasa_key,
    'hd':True,
    'date':'2022-01-19',
    }
    response=requests.get(url,params=params)
    json_data=json.loads(response.text)
    print(json_data)

    img_nasa=json_data['url']
    webbrowser.open(img_nasa)


def command():
   r = sr.Recognizer()
   with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
   

   try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

   except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
   return query


def wish():
    hour = int(datetime.datetime.now().hour)
    # hour=17
    if hour >= 5 and hour <= 12:
        speak("good morning ")
    elif hour >= 12 and hour <= 16:
        speak("good afternoon")
    elif hour >= 17 and hour <= 20:
        speak("good evening")
    elif hour >= 20 and hour <= 4:
        speak("good night")
    speak("hello sir myself astra !! please tell me how can i help you")



def weather_get(a):
    


    speak(("collecting data"))
    weather_key="b7d296dee52558fbe716de8249e0be84"

    url="https://api.openweathermap.org/data/2.5/weather"
    params={
        "APPID":weather_key,
        'q':a,
        'units':'imperial'
    }
    response=requests.get(url,params=params)
    # json_data=json.loads(response.text)
    # print(json_data)
    print(response.json())
    wea=response.json()

    try:
        city=(wea['name'])
        description=(wea['weather'][0]['description'])
        temp=(wea["main"]['temp'])
        tem_in_celcius=(temp - 32) * 5/9
        temp=("%.2f")%tem_in_celcius

        speak(f"right now its {temp} celsius in {city} the day will be {description} ")
    except Exception as a:
        speak("no city found")





# def name():
#     if "astra" in query :
def read():
    speak("do you want to read a particular note or all note")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio3 = r.listen(source,timeout=5,phrase_time_limit=8)
        query4 = r.recognize_google(audio3, language="en-in")
    if "all" in query4:
        with open('notes.txt','r') as g:
            a=g.readlines()


            for line in a[1]:

                 speak(line)



    elif "particular" in query4:
        pass

def mars_images():
    speak("collecting data from nasa")
    nasa_key='GRyc9JMQDZyThfvk6qbsXnDZpQla7mXZs6AJ9CXT'
    url=f'https://api.nasa.gov/mars-photos/api/v1/rovers/perseverance/latest_photos?api_key={nasa_key}'
    response=requests.get(url)
    r=response.json()
    # print(r)
    all_img=(r['latest_photos'])
    print(all_img)
    a=0
    for img in all_img:
        a+=1
        if img['img_src']!='https://mars.nasa.gov/mars2020-raw-images/pub/ods/surface/sol/00325/ids/edr/browse/zcam/ZR4_0325_0695784031_013EBY_N0090000ZCAM03298_1100LMJ01_1200.jpg':
            webbrowser.open(img['img_src'])
            if a==15:
                break

def add():
    speak("in how many parts you want to divide your notes")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio2 = r.listen(source,timeout=5,phrase_time_limit=8)
        query3 = r.recognize_google(audio2, language="en-in")
        Lines = (w2n.word_to_num(query3))
        print(f"User said:{Lines}")

    a = 1
    with open('notes.txt', 'a') as c:
        l = datetime.datetime.now()
        c.write("Date:%s/%s/%s" % (l.date, l.month, l.year))
        c.write("TIME:%s:%s:%s \n" % (l.hour, l.minute, l.second))
    for n in range(Lines):
        speak("say your" + num2words(n, to="ordinal") + "st note")
        with sr.Microphone() as source:
            print("Listening.....")
            r.pause_threshold = 1
            audio3 = r.listen(source,timeout=5,phrase_time_limit=8)
            query4 = r.recognize_google(audio3, language="en-in")
            print(f"User said:{query4}")
        with open('notes.txt', 'a') as c:
            c.write(f"{a}.{query4}\n")
            a += 1



if __name__ == "__main__":

    wish()
    while True:
            query=command().lower()
            if "wikipedia" in query:
                query = query.replace("astra", "")
                query = query.replace("Astra", "")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                print(results)
                speak(results)

            elif "open youtube" in query:

                # webbrowser.register('chrome', None)
                query = query.replace("astra", "")
                query = query.replace("Astra", "")
                webbrowser.register('chrome', None,
                webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))
                webbrowser.get('chrome').open("youtube.com")
                # webbrowser.open("youtube.com",new=2)

            elif "weather" in query or "whether" in query:
                    query=query.replace("weather in","")
                    # query=query.replace("in","")
                    # query=query.replace("whether","")
                    weather_get(query)
                    print(query)


            elif "station" in query:
                iss()
            # speak("seraching")

            elif "open email" in query:

                query = query.replace("astra", "")
                query = query.replace("Astra", "")
                webbrowser.register('chrome', None,
                webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))

                webbrowser.get('chrome').open("gmail.com")
            elif "rock" in query:
                game()
            elif "open google" in query:
                query = query.replace("astra", "")
                query = query.replace("Astra", "")
                webbrowser.register('chrome', None,
                webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))
                webbrowser.get('chrome').open("google.com")

            elif "valorant" in query:
                valorant = "C:\\Riot Games\\Riot Client\\RiotClientServices.exe"
                print(f"User said:{query}")
                os.startfile(valorant)

            elif "code" in query:
                code = "D:\\PyCharm Community Edition 2021.3.1\\bin\\pycharm64.exe"
                os.startfile(code)

            elif "search" in query:

                query = query.replace("stella", "")
                query = query.replace("Stella", "")
                query = query.replace("search", "")
                print(f"User said:{query}")
                webbrowser.register('chrome', None,webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))
                webbrowser.get('chrome')
                pk.search(query)
                # for a in range(1):
            elif "asteroid" in query:
                asteroid()
            elif "open linkedin" in query:


                query = query.replace("astra", "")
                query = query.replace("Astra", "")
                webbrowser.register('chrome', None,
                webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))
                webbrowser.get('chrome').open("https://www.linkedin.com/feed/")


            elif "ipod" in query or "apod" in query:
                nasa_apod()


            elif "mars images" in query:
                mars_images()

            elif "time" in query:
                q = datetime.datetime.now()
                speak("%s:%s" % (q.hour, q.minute))



            elif "date" in query:
                e = datetime.datetime.now()
                speak("%s/%s/%s" % (e.month, e.day, e.year))

            # elif "who" in query:
            #     speak("me hemant hu!!muje abhiraj ne banaya hu python ke madad se")
            #     break
            elif "spotify" in query:
                location = "C:\\Users\\Mayur\\AppData\\Roaming\\Spotify\\Spotify.exe"
                os.startfile(location)
            elif "sleep" in query:
                speak("ok sir,i am going to sleep you can call me anytime")
                break

            elif "created" in query:
                speak("i am the creation of abhiraj sir!!he created me using python!!my job is to make peoples life easier")

            elif "message" in query:
                pywhatkit.sendwhatmsg('7470563122','hello from stella',time_hour=20,time_min=9)
                speak("your msg will send on time")


            elif "play" in query:
                query = query.replace("songs on youtube", "")
                kit.playonyt(query)

            if "notes" in query:
                speak("say paasword")
                password = "universe"
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print("Listening...")
                    r.pause_threshold = 1
                    input2 = r.listen(source,timeout=5,phrase_time_limit=8)
                    query3 = r.recognize_google(input2, language="en-in").lower()

                print(f"User said:{query3}")
                if "cosmic" in query3:
                    speak("Do you want to add something to notes or want to read it")
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
                        print("Listening...")
                        r.pause_threshold = 1
                        input1 = r.listen(source,timeout=5,phrase_time_limit=8)
                        query1 = r.recognize_google(input1, language="en-in").lower()
                        print(f"User said:{query1}")
                    if "read" in query1:
                        read()

                    elif "ad" in query1:
                        add()

                else:
                    speak("wrong password")
            elif "calculator" in query:
                speak("activating calculator")
                speak("calculator activated")
                speak("say your first number sir")
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print("Listening.....")
                    r.pause_threshold = 1
                    audio3 = r.listen(source,timeout=5,phrase_time_limit=8)
                    query4 = r.recognize_google(audio3, language="en-in")
                num1=w2n.word_to_num(query4)
                print(f"User said:{query4}")
                speak("which operation you want to perform")
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print("Listening.....")
                    r.pause_threshold = 1
                    audio4 = r.listen(source,timeout=5,phrase_time_limit=8)
                    query5 = r.recognize_google(audio4, language="en-in")
                print(f"User said:{query5}")
                speak("say your second number")
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print("Listening.....")
                    r.pause_threshold = 1
                    audio5 = r.listen(source,timeout=5,phrase_time_limit=8)
                    query6 = r.recognize_google(audio5, language="en-in")
                    num2=w2n.word_to_num(query6)

                if "divide" in query5 or "division" in query5:
                    num_result=num1/num2
                    speak(f"result is{num_result}")
                elif "multiply"  in query5 or "multiplication"  in query5:
                    num_result=num1*num2
                    speak(f"result is{num_result}")
                elif "sum" in query5 or "ad" in query5:
                    num_result=num1+num2
                    speak(f"result is{num_result}")
                elif  "minus" in query5 or "subtract" in query5:
                    num_result=num1-num2
                    speak(f"result is{num_result}")





        # elif "read" in query1 :
        #         read()
