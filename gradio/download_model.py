# from huggingface_hub import hf_hub_download

# hf_hub_download(repo_id='gpt2', filename='config.json', cache_dir='/home/y/Documents/model/gpt2')

from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained('gpt2')
tokenizer.save_pretrained('/home/y/Documents/model/gpt2')

