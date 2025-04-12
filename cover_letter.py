import requests
import gradio as gr
import os
from dotenv import load_dotenv

# Paste your Hugging Face access token here
load_dotenv()

API_TOKEN = os.getenv("HF_API_TOKEN")
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"


headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

def query_huggingface_api(prompt):
    payload = {
        "inputs": prompt,
        "parameters": {"max_new_tokens": 256, "temperature": 0.7}
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()[0]["generated_text"]

# Cover letter generator function
def generate_cover_letter(company_name, position_name, job_description, resume_content):
    prompt = (
        f"Write a professional and personalized cover letter for the company '{company_name}' "
        f"for the position of '{position_name}'. "
        f"Use the following job description:\n{job_description}\n\n"
        f"And base it on the following resume content:\n{resume_content}\n\n"
        f"Make sure to highlight how the resume aligns with the job role."
    )
    return query_huggingface_api(prompt)

# Gradio Interface
cover_letter_app = gr.Interface(
    fn=generate_cover_letter,
    inputs=[
        gr.Textbox(label="Company Name"),
        gr.Textbox(label="Position Name"),
        gr.Textbox(label="Job Description", lines=10),
        gr.Textbox(label="Resume Content", lines=10),
    ],
    outputs=gr.Textbox(label="Generated Cover Letter", lines=20),
    title="Customized Cover Letter Generator",
    description="Generate a customized cover letter by entering the company name, position name, job description and your resume."

)

cover_letter_app.launch()
