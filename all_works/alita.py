import speech_recognition as s_r
import pyttsx3
import sys


def talk_alita(talk):
    engine = pyttsx3.init()
    engine.say(talk)
    engine.runAndWait()


talk_alita("Hi boss I am waiting commands")


def command():
    r = s_r.Recognizer()

    with s_r.Microphone(device_index=1) as source:
        audio = r.listen(source)

    try:
        task = r.recognize_google(audio, language="en-EN").lower()
        print(f"[log] I am listening: {task}")

    except:
        talk_alita("I am not listening you!, please try again")
        task = command()

    return task


def working(task):
    if "hi alita" in task:
        talk_alita("Hi")

    elif "stop" in task:
        talk_alita("stopping")
        sys.exit()


while True:
    working(command())