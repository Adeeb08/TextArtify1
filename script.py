
#### `script.py`
#This is your main Python script.
#```python
import gradio as gr
import io
import requests
from PIL import Image
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
API_KEY = os.getenv('HUGGINGFACE_API_KEY')

API_URL = "https://api-inference.huggingface.co/models/sd-community/sdxl-flash"
headers = {"Authorization": f"Bearer {API_KEY}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.content
    else:
        raise Exception(f"Failed to fetch image: {response.status_code} {response.text}")

def generate_image(prompt):
    try:
        image_bytes = query({"inputs": prompt})
        image = Image.open(io.BytesIO(image_bytes))
        return image
    except Exception as e:
        print(e)
        return None

demo = gr.Interface(
    fn=generate_image,
    inputs="text",
    outputs="image"
)

demo.launch(share=True)
