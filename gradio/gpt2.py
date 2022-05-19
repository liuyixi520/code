from transformers import pipeline
import gradio as gr

model = pipeline(task='text-generation', model='gpt2')


def predict(prompt):
    completion = model(prompt)[0]["generated_text"]
    return completion

gr.Interface(fn=predict, inputs="text", outputs="text").launch()