# -*- coding: utf-8 -*-
import eel
@eel.expose
def test_print(str):
    
    print("进来了",str)
    test_process(str)  #python 中的处理过程，再调用js中的函数返回
    
    
def test_process(str):
    str2 = str+'已处理'
    eel.system_sends_message2(str2)  # 调用js文件里的函数，将结果返回去

def my_add(a, b):
    return a+b

def say_hello_py(x):
    print(f'Hello {x}')

# eel.say_hello_js('test')

if __name__ == '__main__':
    eel.init("/home/y/Documents/code")
    eel.start("test.html")
