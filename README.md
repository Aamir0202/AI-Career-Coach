
# 🤖 AI Career Coach

An intelligent, cloud-based assistant built using **Mistral-7B**, **Gradio**, and **Hugging Face**. AI Career Coach helps job seekers enhance their resumes, generate personalized cover letters, and get expert-level career advice — all powered by state-of-the-art LLMs.

## 🚀 Features

### 🧠 Career Advisor (`career_advisor.py`)
- Analyze job descriptions and your resume content.
- Get tailored career advice to align your resume with the role you're applying for.
- Receive actionable feedback to boost your selection chances.

### 📄 Resume Enhancer (`resume_enhancer.py`)
- Upload your resume content.
- Let the AI review and suggest improvements, optimized for clarity, impact, and relevance.
- Get tips to strengthen formatting, achievements, and skills section.

### 💌 Cover Letter Generator (`cover_letter_generator.py`)
- Enter the job title, description, and resume highlights.
- Instantly generate a personalized, role-specific cover letter that stands out.

---

## ⚙️ Technologies Used

- **Mistral-7B (via Hugging Face Inference API)** – Instruction-tuned LLM for generating high-quality, context-aware content.
- **Gradio** – Interactive UI for real-time feedback and input/output handling.

---

## 📁 File Structure

```
├── career_advisor.py              # Real-time resume and job description analysis
├── resume_enhancer.py            # Resume improvement suggestions
├── cover_letter_generator.py     # Custom cover letter creation
├── .env                          # Hugging Face API token
└── requirements.txt              # Python dependencies
```

---

## 🛠️ Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Aamir0202/AI-Career-Coach.git
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Add your Hugging Face API Token:**
   Create a `.env` file and add:
   ```
   HF_API_TOKEN=your_huggingface_token_here
   ```

4. **Run any module:**
   ```bash
   python cover_letter.py
   ```

## 📬 Connect

Made with 💙 by [Aamir](https://www.linkedin.com/in/aamir0202)

If you find this project helpful, give it a ⭐ and feel free to contribute or open an issue!

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
