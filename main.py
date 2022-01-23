
import speech_recognition as sr
from time import ctime
import time
import playsound
import os
import random
from gtts import gTTS #not working on windows (no problem found on mac & linux)  you can use (pyTTsx) instead
import webbrowser


r = sr.Recognizer()


def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice_data = ""
        try:
            voice_data = r.recognize_google(audio)
            print(voice_data)
        except sr.UnknownValueError:
            print("sorry i did not get that")
        except sr.RequestError:
            print("sorry, my speech service is down")
        return voice_data


# def lara_speak(audio_string):
#     #tts = gTTS(text=audio_string, lang='en')
#     #r = random.randint(1, 10000000)
#     #audio_file = str(r) + '.mp3'
#     # tts.save(audio_file)
#     playsound.playsound(audio_string)

#replace lara_speak function with (print) because of some compatibility problems in Google text to speech library with windows commands (no problem found on mac & linux)
def respond(voice_data):
    if "name" in voice_data:
        print("my name is lara") #replaced

    if "what time is it" in voice_data:
        print(ctime()) #replaced
    if "search" in voice_data:

        search = record_audio("what do you want to search for ?")
        url = "https://google.com/search?q=" + search
        webbrowser.get().open(url)
        print("here is what i found for " + search) #replaced

    if "find a location" in voice_data:

        location = record_audio("what is the location you are looking for")
        url = "https://google.nl/maps/place/" + location + "/&amp;"
        webbrowser.get().open(url)
        print("here is the location of " + location) #replaced

    if "sleep" in voice_data:
        print("good bye") #replaced

        exit()


time.sleep(1)
print("how can I help you ?") #replaced
while 1:
    voice_data = record_audio()
    respond(voice_data)
