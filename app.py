import streamlit as st
from dotenv import load_dotenv
import os
import io
import PyPDF2
import google.generativeai as genai

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# -----------------------------
# Gemini response function
# -----------------------------
def get_gemini_response(prompt_text, pdf_text, job_description):
    """
    Send prompt + PDF content + job description to Gemini Pro
    """
    model = genai.GenerativeModel("gemini-2.5-flash")
    full_prompt = f"{prompt_text}\n\nPDF Content:\n{pdf_text}\n\nJob Description:\n{job_description}"
    response = model.generate_content(full_prompt)
    return response.text

# -----------------------------
# Extract text from PDF
# -----------------------------
def extract_pdf_text(uploaded_file, max_pages=10):
    """
    Extract text from uploaded PDF (limit to max_pages pages)
    """
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    num_pages = min(len(pdf_reader.pages), max_pages)
    text = ""
    for i in range(num_pages):
        page = pdf_reader.pages[i]
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text.strip()

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="ATS Resume Expert")
st.header("ATS Tracking System")

job_description = st.text_area("Job Description:")
uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

# Buttons
analyze_button = st.button("Review Resume")
percentage_button = st.button("Percentage Match")

# Prompts
review_prompt = """
You are an experienced Technical Human Resource Manager. 
Please review the resume provided against the job description. 
Highlight strengths and weaknesses and provide a professional evaluation.
"""

percentage_prompt = """
You are a skilled ATS (Applicant Tracking System) scanner. 
Evaluate the resume against the job description. Provide: 
1. Percentage match
2. Missing keywords
3. Final thoughts
"""

if uploaded_file is not None:
    pdf_text = extract_pdf_text(uploaded_file)

    if analyze_button:
        if pdf_text:
            with st.spinner("Generating evaluation..."):
                response = get_gemini_response(review_prompt, pdf_text, job_description)
            st.subheader("Evaluation:")
            st.write(response)
        else:
            st.warning("No text could be extracted from the PDF.")

    if percentage_button:
        if pdf_text:
            with st.spinner("Calculating percentage match..."):
                response = get_gemini_response(percentage_prompt, pdf_text, job_description)
            st.subheader("Percentage Match & Keywords:")
            st.write(response)
        else:
            st.warning("No text could be extracted from the PDF.")
else:
    st.info("Please upload a PDF to analyze.")
