import pyttsx3 #Text to Speech Recognition
import speech_recognition as sr #Speech to Text Recognition
import datetime
import wikipedia as wikipedia
import webbrowser
import os

engine  = pyttsx3.init('sapi5') # text to Speech Recognition 
voices = engine.getProperty('voices')
#print(voice[0].id)

engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)

def speak(audio):
    '''This function takes text and returns voice
    Args: text
    '''
    engine.say(audio)
    engine.runAndWait()

speak('Hello Jayram, How are you?')    

def takeCommand():
    '''This function takes speech and returns text
    Args: audio
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening....')
        r.pause_threshold = 1
        audio = r.listen(source, timeout=3, phrase_time_limit=5)
        
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language= 'en-in')
        print("Let's talk about {}.".format(query))
    except Exception as e:
        print("voice not recognized")  


takeCommand()

