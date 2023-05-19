import smtplib
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import pyautogui
import requests
import winsound
import cv2
import keyboard 


print('Loading your AI personal assistant - Jojo')

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')


def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Sorry, please say that again")
            return "None"
        return statement

speak("Loading your AI personal assistant jojo")
wishMe()


if __name__=='__main__':


    while True:
        frequency = 500  # Set frequency to 2500 hertz
        duration = 300  # Set duration to 500 milliseconds
        winsound.Beep(frequency, duration)
        statement = takeCommand().lower()
        if statement==0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('your personal assistant jojo is shutting down,Good bye')
            print('your personal assistant jojo is shutting down,Good bye')
            break



        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement = statement.replace("wikipedia", "").strip() # remove leading/trailing spaces
            if statement:
                try:
                    results = wikipedia.summary(statement, sentences=3)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)
                except wikipedia.exceptions.WikipediaException as e:
                    print("Error: ", e)
                    speak("Sorry, I could not find any results on Wikipedia.")
            else:
                speak("Please provide a search term after 'wikipedia'.")


        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google search is open now")
            time.sleep(5)
        elif 'open file explorer' in statement:
            os.startfile("explorer.exe")
            

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            # time.sleep(5)
            if 'compose email' in statement:
            # wait for the page to load
            #   time.sleep(5)
              # click on the compose button
                pyautogui.click(x=75, y=160)
              # wait for the compose window to appear
                time.sleep(5)
              # type the email recipient
                pyautogui.typewrite('recipient@gmail.com')
              # press tab to go to the subject field
                pyautogui.press('tab')
              # type the subject
                pyautogui.typewrite('Subject of the email')
              # press tab to go to the body field
                pyautogui.press('tab')
              # type the body of the email
                pyautogui.typewrite('Body of the email')
              # press ctrl + enter to send the email
                pyautogui.hotkey('ctrl', 'enter')
                speak("Email sent successfully")
              
        # elif "send email" in statement:
        #         # Get the email recipient and message from the user
        #         print("To whom should I send the email?")
        #         engine.say("To whom should I send the email?")
        #         engine.runAndWait()
        #         recipient = input()
        #         print("What should the message say?")
        #         engine.say("What should the message say?")
        #         engine.runAndWait()
        #         message = input()

        #         # Set up the email server and login credentials
        #         server = smtplib.SMTP('smtp.gmail.com', 587)
        #         server.starttls()
        #         server.login('kasera.ssk@gmail.com', 'Asdf##@@111')

        #     # Create the email message
        #         subject = "Message from your voice assistant"
        #         body = message
        #         email = f"Subject: {subject}\n\n{body}"

        #     # Send the email
        #         server.sendmail('kasera.ssk@gmail.com', recipient, email)
        #         print("Email sent!")
        #     # Use the text-to-speech engine to speak the response
        #         engine.say("Email sent!")
        #         engine.runAndWait()
        
        elif "set alarm" in statement or "set an alarm" in statement:
            # Get the time for the alarm from the user
            print("What time should I set the alarm for?")
            speak("What time should I set the alarm for?")
            time = takeCommand()
            # Convert the time to a 24-hour format
            if "am" in time:
                time = time.replace("am", "")
            elif "pm" in time:
                time = time.replace("pm", "")
                time_parts = time.split(":")
                hour = int(time_parts[0]) + 12
                time = f"{hour}:{time_parts[1]}"
            # Set the alarm using the Windows Task Scheduler
            os.system(f"schtasks /create /tn Alarm /tr \"cmd /c start {os.getcwd()}\\alarm.wav\" /sc once /st {time}")
            print(f"Alarm set for {time}.")
            # Use the text-to-speech engine to speak the response
            speak(f"Alarm set for {time}.")
            

        elif "what is weather today" in statement or "give me todays weather report" in statement:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"] - 273.15
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Today's Temperature is" +
                      str(current_temperature) + "degree celsius" +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in Degree Celsius = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")



        elif 'current time' in statement or 'what time now' in statement:
            strTime=datetime.datetime.now().strftime("%I:%M %p").lower()
            strTime = strTime.lstrip("0").replace(" 0", " ")
            speak(f"the time is {strTime}")
        elif 'left click' in statement:
            pyautogui.click()
            speak("Left clicked")
        elif 'right click' in statement:
            pyautogui.rightClick()
            speak("Right clicked")
        elif 'double click' in statement:
            pyautogui.doubleClick()
            speak("Double clicked")
        
        
        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am jojo version 1 point O your persoanl assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
                  'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')


        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Saurabh Kumar Sir")
            print("I was built by Saurabh Kumar Sir")

        elif "open stack overflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")

        elif 'news' in statement or 'show me some news' in statement or 'show me todays news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        elif "open camera" in statement or "take a photo" in statement:
            # ec.capture(0,"robo camera","img.jpg")
            speak("Opening camera")
             # Create an instance of the VideoCapture class
            cap = cv2.VideoCapture(0)
            while True:
                # Capture the video frame by frame
                ret, frame = cap.read()
                # Display the resulting frame
                cv2.imshow('frame', frame)
                # Check if the Tab key is pressed
                if cv2.waitKey(3) == 9:
                   # Release the capture and destroy the OpenCV window
                   cap.release()
                   cv2.destroyAllWindows()
                   speak("Photo captured and saved")
                   # Define the path to the downloads folder
                   downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
                   # Define the filename as the current timestamp
                   filename = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".jpg"
                   # Save the image to the downloads folder
                   cv2.imwrite(os.path.join(downloads_path, filename), frame)
                   break
            speak("Camera closed")
        
            
        elif 'search'  in statement:
            statement = statement.replace("search", "").strip().replace(" ", "+")
            url = f"https://www.google.com/search?q={statement}"
            webbrowser.open_new_tab(url)
            time.sleep(5)

        elif 'ask me something' in statement or "what can you answer" in statement:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question=takeCommand()
            app_id="R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)
        
        elif 'open virtual mouse' in statement:
            speak('opening virtual mouse..')
            # os.startfile("python Virtual_Mouse.py")
            subprocess.Popen(["python", "Virtual_Mouse.py"], shell=True)

        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

time.sleep(3)