# AI-powered-ATS-Resume-Screener

A Streamlit web app that uses Google's **Gemini API** to evaluate a resume against a job description, the way an Applicant Tracking System (ATS) and a technical recruiter would.

Upload a PDF resume, paste a job description, and get either a professional review or a percentage match with the keywords you're missing.

---

## ✨ Features

- **📝 Resume Review:** an evaluation from the perspective of an experienced Technical HR Manager, highlighting strengths, weaknesses and overall fit for the role
- **📊 Percentage Match:** an ATS-style scan that returns:
  1. A percentage match score
  2. Missing keywords from the job description
  3. Final thoughts and recommendations
- **📎 PDF upload:** extracts text from text-based PDF resumes (first 10 pages)
- **⚠️ Helpful messages:** clear warnings when no PDF is uploaded or no text can be extracted


## ⚙️ How It Works

```
Resume (PDF) ──► PyPDF2 text extraction ──┐
                                          ├──► Prompt + Resume + Job Description ──► Gemini 2.5 Flash ──► Results in Streamlit
Job Description (text) ───────────────────┘
```

1. **Extract:** PyPDF2 reads the uploaded PDF and extracts text from up to 10 pages.
2. **Prompt:** the resume text and job description are combined with a role-specific prompt (HR Manager review or ATS scanner).
3. **Analyse:** the combined prompt is sent to **Gemini 2.5 Flash** through the `google-generativeai` SDK.
4. **Display:** Streamlit shows the evaluation or match results.

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| Language | Python |
| Web framework | Streamlit |
| LLM | Google Gemini 2.5 Flash (`google-generativeai`) |
| PDF parsing | PyPDF2 |
| Configuration | python-dotenv |

---

## 🧩 Limitations & Future Improvements

- Scanned (image-only) PDFs are not supported yet; adding OCR would fix this.
- Return the match score as **structured JSON** so it can be shown as a progress bar or chart.
- Support **DOCX** resumes.
- Compare one resume against **multiple job descriptions** at once.

---

## 👤 Author

**Mounish Shanmugam**
MSc Artificial Intelligence & Machine Learning, University of Birmingham
[LinkedIn](https://www.linkedin.com/in/mounish-shanmugam-5a4590233) · [GitHub]([https://github.com/<your-username>](https://github.com/mounish-shanmugam24))
