import gradio as gr

def greet(name):
    return f"Hello, {name}"

demo = gr.Interface(fn=greet, 
                    inputs=gr.Textbox(lines=3, placeholder='Enter your name'),
                    outputs='text')

demo.launch()