from agentpro import AgentPro
from agentpro.tools import AresInternetTool, CodeEngine
import requests
from bs4 import BeautifulSoup
import PyPDF2
import io
import docx
from typing import Dict, List, Optional


def convert_drive_url(url: str) -> str:
    if "drive.google.com" in url and "view" in url:
        file_id = url.split("/d/")[1].split("/")[0]
        return f"https://drive.google.com/uc?export=download&id={file_id}"
    return url


class HiringAgent:
    def __init__(self):
        self.agent = AgentPro(tools=[AresInternetTool(), CodeEngine()])
        
    def extract_text_from_pdf(self, pdf_url: str) -> str:
        """Extract text from PDF file."""
        try:
            pdf_url = convert_drive_url(pdf_url)
            response = requests.get(pdf_url)
            pdf_file = io.BytesIO(response.content)
            reader = PyPDF2.PdfReader(pdf_file)
            text = "\n".join(page.extract_text() or "" for page in reader.pages)
            return text or "⚠️ No text could be extracted from the PDF."
        except Exception as e:
            return f"⚠️ Error reading PDF: {str(e)}"

    def extract_text_from_docx(self, docx_url: str) -> str:
        """Extract text from DOCX file."""
        try:
            docx_url = convert_drive_url(docx_url)
            response = requests.get(docx_url)
            docx_file = io.BytesIO(response.content)
            doc = docx.Document(docx_file)
            text = "\n".join(p.text for p in doc.paragraphs)
            return text or "⚠️ No text found in DOCX."
        except Exception as e:
            return f"⚠️ Error reading DOCX: {str(e)}"

    def analyze_github_profile(self, github_url: str) -> Dict:
        """Analyze GitHub profile and extract relevant information."""
        response = requests.get(github_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        name = soup.find('span', {'class': 'p-name'})
        bio = soup.find('div', {'class': 'p-note'})

        repos = []
        for repo in soup.find_all('a', {'data-hovercard-type': 'repository'})[:5]:
            repos.append({
                'name': repo.text.strip(),
                'url': f"https://github.com{repo['href']}"
            })

        return {
            'name': name.text.strip() if name else "",
            'bio': bio.text.strip() if bio else "",
            'repositories': repos
        }

    def analyze_candidate(self, resume_url: str, github_url: str, job_description: str, company_info: str) -> Dict:
        """Analyze candidate profile and generate assessment."""

        # Resume Extraction
        if resume_url.endswith('.pdf'):
            resume_text = self.extract_text_from_pdf(resume_url)
        elif resume_url.endswith('.docx'):
            resume_text = self.extract_text_from_docx(resume_url)
        else:
            resume_text = "⚠️ Unsupported resume format. Please upload a .pdf or .docx file."

        # GitHub Info
        github_data = self.analyze_github_profile(github_url)

        prompt = f"""
        Analyze this candidate profile and provide a detailed assessment:

        📄 Resume Content:
        {resume_text}

        👨‍💻 GitHub Profile:
        Name: {github_data['name']}
        Bio: {github_data['bio']}
        Top Repositories: {[repo['name'] for repo in github_data['repositories']]}

        📝 Job Description:
        {job_description}

        🏢 Company Information:
        {company_info}

        Please provide:
        1. Skills and experience match with job requirements
        2. Technical proficiency assessment
        3. Cultural fit analysis
        4. Strengths and areas for development
        5. Final hiring recommendation
        """

        assessment = self.agent(prompt)

        return {
            'resume_analysis': resume_text,
            'github_analysis': github_data,
            'assessment': assessment
        }