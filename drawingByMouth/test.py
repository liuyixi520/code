# 再试一下google的翻译
from googletrans import Translator
text_zh = '你吃了么？'
text_en = 'Did you eat?'
host = 'https://translate.google.com'
proxy = {'https': 'localhost:1089'}
translator = Translator(proxies=None)
print(f'中译英：{translator.translate(text_zh, dest="en").text}')
print(f'英译中：{translator.translate(text_en, dest="zh-cn").text}')

