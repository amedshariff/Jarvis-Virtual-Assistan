import speech_recognition as sr
import pyttsx3
import webbrowser as web
import musicLib
import time;

# text to speek method
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    # engine.runAndWait()
    # engine.stop()
    engine.startLoop()
    engine.endLoop()

# speech to text 
r = sr.Recognizer()
def recognize():
    try:
        with sr.Microphone() as source:
            audio = r.listen(source,timeout=1, phrase_time_limit=5)
            text = r.recognize_google(audio)
            return text
    except sr.UnknownValueError:
        return "jarvis"
        # print("didnt understood")
    except sr.RequestError:
        return ""
        # print("didnt understood")
    except Exception as e:
        return ""
        # print("didnt understood")

def work(c):
    chrome= web.BackgroundBrowser(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
    if(c.lower()=="open chrome"):
        chrome.open("https://www.google.com")
    elif(c.lower()=="open youtube"):
        chrome.open("https://www.youtube.com")
    elif(c.lower()=="open chatgpt"):
        chrome.open("https://chat.openai.com")
    elif("play" in c.lower().split(" ")):
        word=c.lower().split(" ")
        link=musicLib.music.get(word[1])
        chrome.open(link)
    elif(c.lower() =="what can you do"):
        speak("i can open specified webpage and play any song")
        print("jcjwkjn")


if __name__ == "__main__" :
    print("__J_A_R_V_I_S__ Activated")
    speak("jarvis activated")
    while True:
        print("listening .....")
        text=recognize()
        if (text.lower()=="jarvis"):
            # print("tell me")
            engine.say("yes")
            engine.runAndWait()
            print("yes")
            text1=recognize()
            work(text1)
        else:
            continue