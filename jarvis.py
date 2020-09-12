import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pywhatkit as kit
import browserhistory
import pyyoutube


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def websiteRecoganizer():
    if '.com' in query:
        webbrowser.open(query)

    elif 'search on google' in query:
        kit.search(query)

    elif 'show my browsing history' in query:
        # bh = browserhistory.get_browserhistory()
        
        # for key,value in bh:
        #     print(key,value)
        pass

def youtubevideoopener(query):
    kit.playonyt(query)
    speak('opening' + query)

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good afternoon!")

    else:
        speak("Good Evening!")

    speak("I am jarvis Sir. Please tell me how may I help you")

def takeCommand():
    # It takes microphone input fromn the user and returns string as output.

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
        print("Say again please...")
        return "None"
    return query

def takeCommands():
    # It takes microphone input fromn the user and returns string as output.

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query2 = r.recognize_google(audio, language='en-in')
        print(f"User said: {query2}\n")

    except Exception as e:
        # print(e)
        print("Say again please...")
        return "None"
    return query2

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('www.moonkhandanger@gmail.com', 'Moonmahan1234')
    server.sendmail('www.moonkhandanger@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        query2 = takeCommands().lower()
        websiteRecoganizer()
        if 'on youtube' in query:
            youtubevideoopener(query)

        # Logic for executing tasks based on query 
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak('opening youtube')
 
        elif 'open google' in query:
            webbrowser.open("google.com")
            speak('opening google')

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com") 

        elif 'open class' in query:
            webbrowser.open("http://eclarcs.in/")
            speak("opening eclarcs")

        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com")
            speak("opening facebook")

        elif 'ertugrul gazi' in query:
            speak('on which platform you would like to see it')
            speak('first on website Giveme5')
            speak('second on website TRT Drama')
            speak('third facebook.com')
            speak('or another websites sir if you are using another website')
            speak('please give me the full link')

            print('on which platform you would like to see it\n'
                'first on website Giveme5\n'
                'second on website TRT Drama\n'
                'third facebook.com\n'
                'or another websites\n'
                'sir,please give me the full link\n')

            link = str(takeCommand)
            webbrowser.open(link)
            speak(f"Opening {link}")

        elif 'play music' in query:
            music_dir = 'E:\\B\\1 ST\\Songs\\English Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to Moon' in query:
            try:
                speak("What shoild I say")
                content = takeCommand
                to = "mkkhandanger48@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Soory moon bhai. I am not able to send the email")

        else:
            speak("Sir where you want to search it")
            takeCommands()
            if query2 == 'google':
                webbrowser.open(query)
                speak('opening google')

            elif query2 == 'youtube':
                youtubevideoopener(query)
                speak('opening youtube')