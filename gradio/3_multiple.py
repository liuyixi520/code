import gradio as gr

def greet(name, is_morning, temperature):
    salutation = 'Good morning' if is_morning else 'Good evening'
    greeting = f'{salutation}, {name}. it is {temperature} degrees.'
    celsius = (temperature - 32) * 5 / 9
    return greeting, celsius

demo = gr.Interface(fn=greet,
                    inputs = ['text', 'checkbox', 'slider'],
                    outputs = ['text', 'number'])
    
demo.launch()