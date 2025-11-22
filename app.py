import streamlit as st
import json
import os

# Paths
EXTRACTED_FILE = "outputs/extracted_text.txt"
SUMMARY_FILE = "outputs/summary_ai.json"
SECTIONS_FILE = "outputs/sections.json"
RULE_REPORT_FILE = "outputs/rules.json"

st.set_page_config(page_title="Universal Credit Act Analyzer", layout="wide")

st.title("⚖️ Universal Credit Act 2025 — Legal AI Analyzer")

st.markdown("Automated legal analysis pipeline using HF models.")

# -------------------------------------------------------------------
# Task Buttons
# -------------------------------------------------------------------

# Run Task 1
if st.button("📄 Run Task 1 — Extract Text"):
    result = os.system("python tasks/task1_extract_pdf.py")
    if os.path.exists(EXTRACTED_FILE):
        st.success("Task 1 Completed — Text Extracted")
        with open(EXTRACTED_FILE, "r", encoding="utf-8") as f:
            st.text(f.read()[:3000])
    else:
        st.error("Task 1 Failed")

# Run Task 2
if st.button("📝 Run Task 2 — Generate Summary"):
    result = os.system("python tasks/task2_summarize_act.py")
    if os.path.exists(SUMMARY_FILE):
        st.success("Task 2 Completed — Summary Generated")
        with open(SUMMARY_FILE, "r", encoding="utf-8") as f:
            st.json(json.load(f))
    else:
        st.error("Task 2 Failed")

# Run Task 3
if st.button("📚 Run Task 3 — Extract Sections"):
    result = os.system("python tasks/task3_extract_sections.py")
    if os.path.exists(SECTIONS_FILE):
        st.success("Task 3 Completed — Sections Extracted")
        with open(SECTIONS_FILE, "r", encoding="utf-8") as f:
            st.json(json.load(f))
    else:
        st.error("Task 3 Failed")

# Run Task 4
if st.button("📊 Run Task 4 — Evaluate Rules"):
    result = os.system("python tasks/task4_rule_checks.py")
    if os.path.exists(RULE_REPORT_FILE):
        st.success("Task 4 Completed — Rule Evaluation Done")
        with open(RULE_REPORT_FILE, "r", encoding="utf-8") as f:
            st.json(json.load(f))
    else:
        st.error("Task 4 Failed")

st.markdown("---")
st.markdown("Made by Priya Kanade — Legal AI Analytics Engine")

