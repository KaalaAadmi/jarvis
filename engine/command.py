import pyttsx3
import speech_recongition as sr
import eel

def speak(text):
    engine=pyttsx3.init('sapi5')
    vocies=engine.getProperty('voices')
    engine.setProperty('voices',voices[1].id)
    engine.setProperty('rate',174)
    engine.say(text)
    engine.runAndWait()

@eel.expose
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone as source:
        print("Listening......")
        eel.DisplayMessage('Listening.....')
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source,10,6)
    try:
        print('Recognizing')
        eel.DisplayMessage('Recognizing')
        query=r.recognize_google(audio,language="en-in")
        print(f"User said: {query}")
        eel.DisplayMessage(query)
        speak(query)
        eel.ShowHood()
    except Exception as e:
        return ""
    return query.lower()


# text=takecommand()

# speak(text)