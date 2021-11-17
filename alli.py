import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import cv2
import random
from requests import get

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour <18:
        speak("good afternoon")
    else:
        speak("good evening")  

    speak("Do tell Alli ! How may I help you")
    speak("listening....")

def takeCommand():
    # take microphone input and return string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language="en-in")
        speak(f"you said: {query}\n")

    except Exception as e:
       speak("Say it again...")
       return "None"
    return query   

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        
       query= takeCommand().lower(); 

       
       if "search" in query:
           speak("searching wikipedia...")
           query = query.replace("search", "")
           results = wikipedia.summary(query, sentences = 5)
           speak(f"According to wikipedia:{results}")

       elif "youtube" in query:
            webbrowser.open("youtube.com")
            
       elif "facebook" in query:
            webbrowser.open("facebook.com")
            
       elif "chrome" in query:
            speak("what are you looking for")
            crom = takeCommand().lower()
            webbrowser.open(f"{crom}")
            
       elif "notes" in query:
            webbrowser.open("keep Notes")
            
       elif "nothing" in query:
            speak("ok")
            
       elif "quit" in query:
            pass
            
       elif "spotify" in query:
            webbrowser.open("spotify")
            
    #    elif "music" in query:
    #         webbrowser.open("Groove Music")
            
       elif "music" in query:
            music_dir = "C:\\Users\\Alligatorr\\Music\\download"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            # for song in songs:
            #     if song.endswith(".mp3"): 
            os.startfile(os.path.join(music_dir, rd))

       elif "time" in query:
           strTime = datetime.datetime.now().strftime("%H:%M:%S")
           speak(f"time is :{strTime}")

       elif "code" in query:
           codePath = "D:\\ File folder\\ anand raj\\Code.exe"
           os.startfile(codePath)
           
       elif "camera" in query:
           cap = cv2.VideoCapture(0)
           while True:
               ret, img = cap.read()
               cv2.imshow("webcam", img)
               k = cv2.waitKey(50)
               if k==27:
                   break;
           cap.release()
           cv2.destroyAllWindows()
                   
           
       elif "ip address" in query:
          ip = get("https://api.ipify.org").text
          speak(f"Your IP address is :{ip}")
      
       elif "send message" in query:
          kit.sendwhatmsg("917494007186", "just checking",2,25)
          