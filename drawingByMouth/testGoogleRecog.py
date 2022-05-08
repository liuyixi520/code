## google的识别
import speech_recognition as sr
r = sr.Recognizer()
with sr.AudioFile('./data/books.wav') as source:
    audio = r.record(source)
    try:
        print(f'google thinks you said : {r.recognize_google(audio)}')
    except sr.UnknownValueError:
        print('google could not understand audio')
    except sr.RequestError as e:
        print('google error; {0}'.format(e))