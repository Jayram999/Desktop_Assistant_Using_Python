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


#speak function
def speak(text):
    """This function takes text and returns voice

    Args:
        text (_type_): string
    """
    engine.say(text)
    engine.runAndWait()


# speech recognition function
def takeCommand():
    """this function will recognize voice & return text
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout  = 5,phrase_time_limit =5)
        '''
        Explanation
        The pause_threshold value is the number of seconds the system will take to recognize the voice after the user has completed their sentence.
        The timeout value is the maximum number of seconds the system will wait for the user to say something before it throws an OSError exception.
        The phrase_time_limit value indicates the number of seconds the user can speak. In this case, it is 5. 
        This means that if the user will speak for more than 5 seconds, that speech will not be recognized.
        '''


        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            print("Say that again please...")
            return "None"
        return query




if __name__ == "__main__":
    
    query = takeCommand().lower()

    if "wikipedia" in query:
        speak("Searching wikipedia")
        query = query.replace('wikipedia', "")
        results = wikipedia.summary(query, sentences = 2)
        speak("According to wikipedia")
        print(results)
        speak(results)

    
    elif "youtube" in query:
        speak("Opening YouTube")
        webbrowser.open("youtube.com")

    
    elif "google" in query:
        speak("Opening google")
        webbrowser.open("google.com")


    elif "github" in query:
        speak("Opening github")
        webbrowser.open("github.com")