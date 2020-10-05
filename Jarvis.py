import pyttsx3
import speech_recognition as sr
import datetime

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') #getting details of current voice
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio) 
    engine.runAndWait()


def system():
    print("SYSTEM : [user not found]")
    print("SYSTEM : [press Enter to enter into JARVIS command protocol]")
    input("....")
    print("SYSTEM : [enter your information to enter into JARVIS command protocol]")
    name = input("enter your name...")
    surname = input("enter your last name...")
    print("enter your passWord below[optional]")
    passWord = input("...")    
    input("press enter to continue...")
    print("SYSTEM : [you are now been installed in JARVIS command protocal]")
    print("")
    print("hold on for a second.......")
    print(f"SYSTEM : [WELCOME {name} {surname} with password {passWord}]") 
    speak(f"welcome {name} {surname}")
    print(f"welcome {name} {surname}")
    #speak("I am JARVIS, your private assistnt")
    #print("I am JARVIS, your private assistnt")
    #speak(f"you can talk with me about anything {name}")
    #print(f"you can talk with me about anything {name}")
    

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good morning my master")
        speak("Good morning my master")
    elif hour>=12 and hour<18:
        print("Good Afternoon")
        speak("Good Afternoon")
    else:
        print("Good Evening")
        speak("Good Evening")
    
    print("I am JARVIS, your private assistant")
    speak("I am JARVIS, your private assistant")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

def takeCommand():
    print("type your command below")
    a = input("...")

    if a == "open youtube":
        print("opeaning youtube")
        webbrowser.open("youtube.com")
    elif a =="open google":
        print("opeaning google")
        webbrowser.open("google.com")
    elif a=="open white hat":
        print("opeaning WhiteHat jr")
        webbrowser.open("WhiteHatJr.com")
    elif a=="open VS code":
        print("openaing Visual studio code")
        codePath = "C:\\Users\\TAO-WSM\\AppData\\Local\\Programs\\Microsoft VS Code"
        os.startfile(codePath)
    
      

if __name__=="__main__" :
    #system()
    wishMe()
    takeCommand()
