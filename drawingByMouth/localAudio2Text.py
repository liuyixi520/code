from numpy import source
import speech_recognition as sr
from translate import Translator

r = sr.Recognizer()
trans_en2zh = Translator(from_lang='english', to_lang='chinese')

# 将本地的音频文件识别为语音
with sr.AudioFile('./data/bird.wav') as source:
    audio = r.record(source)
    try:
        # 如果说的是英文，直接这样就可以了
        text = r.recognize_google(audio, language='en-US')
        print("You said: " + text)
        # 在这里试一下翻译的效果
        trans_text = trans_en2zh.translate(text)
        print(trans_text)
        print(f'你说：{trans_text}')
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
