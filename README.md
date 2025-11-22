# Universal Credit Act 2025 – AI Agent

This project is a mini AI agent that reads and analyzes the **Universal Credit Act 2025** from a PDF and generates a structured legal report in JSON format.

## Features
- ✅ Extracts text from PDF
- ✅ Summarizes the Act using a free Hugging Face model
- ✅ Extracts key legal sections
- ✅ Applies rule-based checks
- ✅ Streamlit UI with one-click execution

## Model Used
- **google/flan-t5-base** (Free, Hugging Face)

## How To Run

1. Activate virtual environment  
venv\Scripts\activate


2. Install dependencies  
pip install -r requirements.txt


3. Run the app
streamlit run app.py


## Outputs
- `extracted_text.txt`
- `summary_ai.json`
- `sections.json`
- `rule_results.json`

## Status
✅ Tasks 1–4 working  
✅ AI integrated  
✅ UI ready  
⏳ Hugging Face deployment (optional)

**Author:** Priya Kanade
