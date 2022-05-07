from numpy import source
import speech_recognition as sr
r = sr.Recognizer()

# 将麦克风的声音识别为文字
with sr.Microphone() as source:
    audio = r.listen(source)
    try:
        print('Recognizing...')
        print("You said: " + r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))