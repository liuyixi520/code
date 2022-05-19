from transformers import pipeline
import gradio as gr

model = pipeline('text-generation')

def predict(text):
    return model(text)[0]['generated_text']

demo = gr.Interface(predict, inputs='text', output='text') 
demo.launch()
