import requests
import gradio as gr
import os
from dotenv import load_dotenv

# Paste your Hugging Face access token here
load_dotenv()

API_TOKEN = os.getenv("HF_API_TOKEN")
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"
#API_URL = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"

headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

def query_huggingface_api(prompt):
    payload = {
        "inputs": prompt,
        "parameters": {"max_new_tokens": 512, "temperature": 0.7}
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()[0]["generated_text"]

# Resume polishing function
def polish_resume(position_name, resume_content, polish_instruction=""):
    if polish_instruction.strip():
        prompt_use = f"Given the resume content: '{resume_content}', polish it based on the following instructions: {polish_instruction} for the {position_name} position."
    else:
        prompt_use = f"Suggest improvements for the following resume content: '{resume_content}' to better align with the requirements and expectations of a {position_name} position. Return the polished version, highlighting necessary adjustments for clarity, relevance, and impact in relation to the targeted role."

    return query_huggingface_api(prompt_use)

# Gradio Interface
resume_polish_app = gr.Interface(
    fn=polish_resume,
    inputs=[
        gr.Textbox(label="Position Name"),
        gr.Textbox(label="Resume Content", lines=15),
        gr.Textbox(label="Polish Instructions (Optional)", lines=2),
    ],
    outputs=gr.Textbox(label="Polished Resume", lines=20),
    title="Resume Polisher",
    description="This application helps you polish your resume. Enter the position your want to apply, your resume content, and specific instructions or areas for improvement (optional), then get a polished version of your content."
)

resume_polish_app.launch()
