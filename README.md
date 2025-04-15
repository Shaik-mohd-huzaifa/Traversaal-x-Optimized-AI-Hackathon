# 🤖 AI-Powered Hiring Agent

This project presents an **agentic hiring assistant** that uses AI to assess candidates based on their resume, GitHub profile, and the job role they are applying for. It combines intelligent data extraction with deep analysis using `AgentPro`, a multi-agent orchestration framework.

---

## 🚀 Features

- 📄 **Resume Parsing**: Supports `.pdf` and `.docx` file URLs to extract text.
- 🧑‍💻 **GitHub Analysis**: Fetches user profile, repositories, and README contents.
- 🧠 **AI-Powered Evaluation**: Uses LLMs to evaluate candidates for job fit, technical depth, and cultural alignment.
- 💡 **Hiring Recommendation**: Returns an internal-style hiring note with observations and decision advice.

---


## 📦 Installation

```bash
# Clone the repo
git clone https://github.com/Shaik-mohd-huzaifa/Traversaal-x-Optimized-AI-Hackathon.git
cd Traversaal-x-Optimized-AI-Hackathon

# (Optional) create and activate virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt
```

Click here to testout : [Live Demo](https://huggingface.co/spaces/Shaikmohdhuz/Hiring_agent)

## Run the App
```
python app.py
```
This will launch a Gradio UI at http://localhost:7860.


---


### Agentic Architecture

![](/image.png)


### Video Demonstration

[Link to the Video](https://youtu.be/e4vXOu2gqH8)
