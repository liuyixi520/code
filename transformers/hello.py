from transformers import pipeline

result = pipeline('sentiment-analysis')('I love you')
print(result)