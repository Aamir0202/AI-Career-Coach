import requests
import gradio as gr
import os
from dotenv import load_dotenv

# Paste your Hugging Face access token here
load_dotenv()

API_TOKEN = os.getenv("HF_API_TOKEN")
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"
#API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
#API_URL = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"

headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

def query_huggingface_api(prompt):
    payload = {
        "inputs": prompt,
        "parameters": {"max_new_tokens": 1024, "temperature": 0.7}
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    print(response.json())
    return response.json()[0]["generated_text"]

# Career advice function
def generate_career_advice(position_applied, job_description, resume_content):
    prompt = (
        f"Considering the job description:\n{job_description}\n\n"
        f"And the resume content:\n{resume_content}\n\n"
        f"Give tailored advice on how to improve the resume to increase chances of being selected for the '{position_applied}' role. "
        f"Include specific suggestions for alignment with the job role."
    )
    return query_huggingface_api(prompt)

# Gradio Interface
career_advice_app = gr.Interface(
    fn=generate_career_advice,
    inputs=[
        gr.Textbox(label="Position Applied For"),
        gr.Textbox(label="Job Description", lines=10),
        gr.Textbox(label="Resume Content", lines=10),
    ],
    outputs=gr.Textbox(label="Career Advice", lines=20),
    title="Career Advisor",
    description="Enter the position you're applying for, paste the job description, and your resume content to get advice on what to improve for getting this job."
)

career_advice_app.launch()
