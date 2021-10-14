import os
import smtplib
import sys
import webbrowser
from datetime import datetime
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import cv2
import instaloader
import pyautogui
import pyttsx3
import pytz
import pywhatkit as kit
import requests
import speech_recognition as sr
import wikipedia
from dask.tests.test_system import psutil
from requests import get
import speedtest
from pywikihow import search_wikihow
import PyPDF2
import winsound






engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('rate', 180)
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# To convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source, phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("...........")
        return "none"
    query = query.lower()
    return query


# to wish
def wish():
    now = datetime.now()
    hours = int(now.strftime("%H"))
    minn = now.strftime("%M")
    sec = now.strftime("%S")

    if hours >= 0 and hours < 12:
        speak("good morning sir")
    elif hours > 12 and hours < 18:
        speak("good afternoon sir")
    else:
        speak("good evening sir")
    speak('The running time is:-')
    if 0 <= hours < 12:
        speak(f" {hours}:{minn} A M")
    elif 12 <= hours < 24:
        speak(f" {hours}:{minn} P M")

    speak("Hello sir i am Alice, your personal study companiyan")
    speak("Please tell me what can i do for you sir")
    speak("I am Listening")


# for news updates
def news():
    main_url = "http://newsapi.org/v2/top-headlines?sources=techcrunch&apikey=bc18fc12962140878b3410478a523f1f"
    main_page = requests.get(main_url).json()
    # print(main_page)
    articles = main_page["articles"]
    # print(articles)
    head = []
    day = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        # print(f"today's {day[i]} news is: ", head[i])
        speak(f"today's {day[i]} news is: {head[i]}")


def pdf_reader():
    book = open("C:\\Users\\RAJESH\\Downloads\\py4.pdf", "rb")
    pdfReader = PyPDF2.PdfFileReader(book)  # pip install PyPDF2
    pages = pdfReader.numPages
    speak(f"Total numbers of pages in this book {pages} ")
    pg = int(input("Please enter the page number: "))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speak(text)



def TaskExecution():
    wish()
    while True:
        # if 1:

        query = takecommand().lower()
        # logic building for tasks
        if "wake up" in query:
            speak("I am up sir")

        elif "date" in query:
            speak("today date is")
            t_date = datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata'))
            speak(t_date.strftime('%d %B , of %y'))

        elif "what is your name" in query or "your name" in query:
            speak("My name is Alice.")

        elif "you marry me" in query:
            speak("I will not able to marry you because i am a function not a human")

        elif "open notepad" in query:
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)
        elif "open command prompt" in query:
            os.system("start cmd")

        elif "open camera" in query:
            speak("ok sir, i am open your wabcam")
            cap = cv2.VideoCapture(0)
            while True:
                ret, ing = cap.read()
                cv2.imshow('webcam', ing)
                k = cv2.waitKey(50)
                if k == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif "play music" in query:
            speak("ok sir, i am playing music")
            music_dir = "E:\\song\\music new"
            songs = os.listdir(music_dir)
            # rd = random.chice(songs)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, songs[0]))
                    break


        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia....")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=5)
            speak("according to wikipedia")
            speak(result)
            # print(result)

        elif "open youtube" in query:
            speak("Ok i am open youtube")
            webbrowser.open("www.youtube.com")


        elif "open facebook" in query:
            speak("Ok i am open facebook")
            webbrowser.open("www.facebook.com")

        elif "open stackoverflow" in query:
            webbrowser.open("www.stackoverflow.com")

        elif "open google" in query:
            speak("Ok sir , I am open the google")
            speak("But")
            speak("sir, what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")
            speak("According to google , i found this results ")

        elif "send message" in query:
            kit.sendwhatmsg("+91958475043", "this is testing protocal", 2, 25)

        elif "play songs on youtube" in query:
            speak("Ok sir , I  am playing  the  song on youtube")
            speak("I hope do you like this song sir")
            kit.playonyt("memorise")


        elif "switch the window" in query:
            speak("OK sir,i am switch the window")
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            pyautogui.keyUp("alt")

        elif "tell me news" in query:
            speak("please wait sir, feteching the latest news")
            news()

        elif "email to gudiya didi" in query:
            speak("what should i say?")
            query = takecommand().lower()
            if "send a file" in query:
                email = "vsrajpurohit0111@gmail.com"  # your email
                password = "vishal3063$"  # your email account password
                send_to_email = "rajpurohitlaxmi93@gmail.com"  # whom you are sending the message to
                speak("okay sir, what is the subject for this email")
                query = takecommand().lower()
                subject = query  # the subject in the email
                query2 = takecommand().lower()
                message = query2  # the message in the email
                speak("sir please enter the correct path here")  # the file attachment in the email
                file_location = input("Enter path here:- ")

                speak("please wait,i am sending email now")

                msg = MIMEMultipart()
                msg["From"] = email
                msg["To"] = send_to_email
                msg["Subject"] = subject

                msg.attach(MIMEText(message, "plain"))

                # setup the  attachment
                filename = os.path.basename(file_location)
                attachment = open(file_location, "rb")
                payload = MIMEBase('application', 'octate-stream')
                payload.set_payload((attachment).read())
                encoders.encode_base64(payload)  # encode the attachment

                # add payload header with filename
                payload.add_header('Content-Decomposition', 'attachment', filename=filename)

                # Attach the attachment to the MIMEMultipart object
                msg.attach(payload)

                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login(email, password)
                text = msg.as_string()
                server.sendmail(email, send_to_email, text)
                server.quit()
                speak("email has send to Leaxmi didi")

            else:
                email = "vsrajpurohit0111@gmail.com"  # your email
                password = "vishal3063$"  # your email account password
                send_to_email = "rajpurohitlaxmi93@gmail.com"  # whom you are sending the message to
                message = query  # the message in the email

                server = smtplib.SMTP("smtp.gmail.com", 587)  # Connect to the server
                server.starttls()  # use tls
                server.login(email, password)  # login to the email server
                server.sendmail(email, send_to_email, message)  # send the email
                server.quit()  # Logout of the email server
                speak("email has been sent to the laxmi didi")

        elif "where i am" in query or "where we are" in query:
            speak("wait sir, let me check")
            try:
                ipAdd = requests.get("https://api.ipify.org").text
                print(ipAdd)
                url = "https://get.geojs.io/v1/ip/geo/" + ipAdd + ".json"
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                # print(geo_data)
                city = geo_data["city"]
                # states = geo_data["state"]
                country = geo_data["country"]
                speak(f"sir i am not sure, but i think we are in {city} city of {country} country")
            except Exception as e:
                speak("sorry sir, Due to network issue i am not able to find where we are.")
                pass

        # -----------------------------To check a instagram profile-------

        elif "instagram profile" in query or "profile on instagram" in query:
            speak("sir please enter the user name correctly.")
            name = input("Enter username here:")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"Sir here is the profile of the user {name}")
            speak("sir would you like to downlode profile picture of this account.")
            condition = takecommand().lower()
            if "yes" in condition:
                mod = instaloader.Instaloader()  # pip install instadownloader
                mod.download_profile(name, profile_pic_only=True)
                speak("I am done sir, profile picture is saved in our main folder. now i am ready for next command")
            else:
                pass


        elif 'battery' in query or "battery states" in query:
            speak('checking battery status')
            battery = psutil.sensors_battery()
            battery_per = battery.percent
            speak(f"your battery is {battery_per} percent charged")
            if battery_per <= 50:
                speak(f"your battery percent is {battery_per}. it is low plese plug in charger")

        elif 'who created you alice' in query or "who created you" in query:
            speak("Vishal Singh had created me. He is my god")

        elif "internet speed" in query:

            speak("I am checking internet speed sir, please wait few second")
            st = speedtest.Speedtest()
            dl = st.download()
            up = st.upload()
            speak(f"sir we have {dl} bit per second  downloading speed and {up} bit per second uploading speed ")

        elif "activate how to do mode" in query:
            speak("How to do mode is activated.")
            while True:
                speak("Please tell me what you want know")
                how = takecommand()
                try:
                    if "exit" in how or "close" in how:
                        speak("Okay sir, how to do mode is closed")
                        break
                    else:

                        max_results = 1
                        how_to = search_wikihow(how, max_results)
                        assert len(how_to) == 1
                        speak(how_to[0].summary)
                except Exception as e:
                    speak("Sorry sir,i am not able to find this")

        # ---------------------------  To take screenshot ------------


        elif "screenshot" in query:
            speak("Sir, please tell me the name for this screenshot file")
            o = takecommand().lower()
            speak("Sir, please hold the screen for few second, i am taking screenshot")
            img = pyautogui.screenshot()
            img.save(f"{o}.png")
            speak("I am done sir, the screenshot is saved in our main folder. Now i am ready for next command")

#------------------------------ To hide files and folder -----------------------------
        elif "hide all files" in query or "hide this folder" in query or "visible for everyone" in query:
            speak("sir please tell me you want to hide this folder or make it visible for everyone")
            condition = takecommand().lower()
            if"hide" in condition:
                os.system("attrib +h/s /d") #os module
                speak("sir,all the files in this folder are now hidden.")

        elif "visible" in query:
            speak("sir,all the files in this folder are now visible to everyone. i wish you are taking")
            condition = takecommand().lower()
            if "visible" in condition:
                os.system("attrib -h/s /d")
                speak("sir,all the files in this folder are now visible.")


            elif "leave it" in condition or "leave for now" in  condition:
                speak("ok sir")





        elif "you can sleep" in query or "sleep now" in query:
            speak("Okay sir, i am going to sleep you can call me anytime.")
            break



        elif "temperature" in query:
            search = "temperature in saja"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = wikipedia.BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"current {search} is {temp}")



        # ------------------To read pdf file-------------------------

        elif "read pdf" in query:
            pdf_reader()

        elif "volume up" in query or "up the volume" in query:
            pyautogui.press("volumeup")

        elif "volume down" in query or "down the volume" in query:
            pyautogui.press("volumedown")

        elif "volume mute" in query or "mute the volume" in query or "mute" in query:
            pyautogui.press("volumemute")

        elif "alarm" in quary:
            speak("sir please tell me the time to set alarm. for example, set alarm to 5:30 am")
            tt = takecommand()                  # set alarm to 5:30 a.m.
            tt = tt.replace("set alarm to ", "") # 5:30 a.m.
            tt = tt.replace(".","") # 5:30 a.m.
            tt = tt.upper() #5:30 AM
            MyAlarm.alarm(tt)






        elif "thank you" in query:
            speak("thank you for using me sir, good day sir")
            sys.exit()

        speak("sir,do you have any other work")




if __name__ == "__main__":
    while True:
        permission = takecommand()
        if "wake up" in permission:
            TaskExecution()

        elif 'goodbye' in permission:
            speak("thanks for using me sir, have a good day")
            sys.exit()
