import gradio as gr
from agent import HiringAgent

# Initialize the hiring agent
hiring_agent = HiringAgent()

def analyze_candidate(resume_url, github_url, job_description, company_info):
    try:
        result = hiring_agent.analyze_candidate(resume_url, github_url, job_description, company_info)
        return result['assessment']
    except Exception as e:
        return f"Error analyzing candidate: {str(e)}"

# Create a simple Gradio Interface
with gr.Blocks(theme=gr.themes.Soft()) as app:
    gr.Markdown("""
    # 🤖 AgentPro Hiring Assistant
    Upload candidate details and get a detailed assessment for your hiring process.
    """)
    
    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("### 📝 Candidate Information")
            resume_url = gr.Textbox(
                label="Resume URL",
                placeholder="Enter Google Drive URL of the resume",
                info="Paste the Google Drive URL of the candidate's resume"
            )
            github_url = gr.Textbox(
                label="GitHub Profile",
                placeholder="Enter GitHub profile URL",
                info="Paste the candidate's GitHub profile URL"
            )
            
            gr.Markdown("### 🏢 Job & Company Details")
            job_description = gr.Textbox(
                label="Job Description",
                placeholder="Enter the job description",
                lines=5,
                info="Describe the role and requirements"
            )
            company_info = gr.Textbox(
                label="Company Information",
                placeholder="Enter company details and culture",
                lines=3,
                info="Describe the company culture and environment"
            )
            
            analyze_btn = gr.Button("Analyze Candidate", variant="primary")
        
        with gr.Column(scale=2):
            gr.Markdown("### 📊 Assessment Results")
            output = gr.Markdown()
    
    # Add example inputs
    gr.Markdown("### 💡 Example Inputs")
    gr.Examples(
        examples=[
            [
                "https://drive.google.com/example-resume.pdf",
                "https://github.com/example-user",
                "Looking for a Senior Python Developer with 5+ years of experience in web development, machine learning, and cloud technologies. Must have strong problem-solving skills and experience with agile methodologies.",
                "Tech startup focused on AI solutions, fast-paced environment, collaborative culture, emphasis on innovation and continuous learning."
            ]
        ],
        inputs=[resume_url, github_url, job_description, company_info],
        outputs=[output],
        fn=analyze_candidate,
        cache_examples=True
    )
    
    # Add footer
    gr.Markdown("""
    ---
    *Powered by AgentPro - An AI-powered hiring assistant*
    """)
    
    # Connect the analyze button
    analyze_btn.click(
        fn=analyze_candidate,
        inputs=[resume_url, github_url, job_description, company_info],
        outputs=[output]
    )

# Launch the app
app.launch(share=True)
