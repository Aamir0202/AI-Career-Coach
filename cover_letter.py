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
        "parameters": {"max_new_tokens": 1024, "temperature": 0.7}
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()[0]["generated_text"]

# Cover letter generator function
def generate_cover_letter(company_name, position_name, job_description, resume_content):
    prompt = f"Generate a customized cover letter using the company name: {company_name}, the position applied for: {position_name}, and the job description: {job_description}. Ensure the cover letter highlights my qualifications and experience as detailed in the resume content: {resume_content}. Adapt the content carefully to avoid including experiences not present in my resume but mentioned in the job description. The goal is to emphasize the alignment between my existing skills and the requirements of the role."
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
