import streamlit as st
import subprocess
import json
import os

st.set_page_config(page_title="Universal Credit Act AI Agent", layout="wide")

st.title("📜 Universal Credit Act 2025 – AI Agent")
st.write("This AI system extracts, summarizes, analyzes, and validates the Universal Credit Act 2025")

open("logs.txt", "w").close()

def run_task(script_name):
    result = subprocess.run(
        ["python", f"tasks/{script_name}"],
        capture_output=True,
        text=True
    )
    with open("logs.txt", "a", encoding="utf-8") as f:
        f.write(result.stdout + "\n" + result.stderr + "\n")
    return result

if st.button("🚀 Run Full AI Pipeline (All Tasks)"):
    with st.spinner("Running Tasks... Please wait..."):
        run_task("task1_extract_text.py")
        run_task("task2_summarize_ai.py")
        run_task("task3_extract_sections.py")
        run_task("task4_rule_checks.py")

    st.success("✅ All tasks completed!")

# Display Summary
if os.path.exists("outputs/summary_ai.json"):
    st.subheader("📌 AI Summary (Task 2)")
    with open("outputs/summary_ai.json", "r", encoding="utf-8") as f:
        summary = json.load(f)

    for s in summary:
        st.write("•", s)

    st.download_button("⬇ Download Summary", json.dumps(summary, indent=2), file_name="summary.json")

# Display Extracted Sections
if os.path.exists("outputs/sections.json"):
    st.subheader("📂 Extracted Sections (Task 3)")
    with open("outputs/sections.json", "r", encoding="utf-8") as f:
        sections = json.load(f)

    st.json(sections)
    st.download_button("⬇ Download Sections", json.dumps(sections, indent=2), file_name="sections.json")

# Display Rule Checks
if os.path.exists("outputs/rules.json"):
    st.subheader("🧠 Rule Validation Results (Task 4)")
    with open("outputs/rules.json", "r", encoding="utf-8") as f:
        rules = json.load(f)

    st.json(rules)
    st.download_button("⬇ Download Rules", json.dumps(rules, indent=2), file_name="rules.json")

# Logs
if os.path.exists("logs.txt"):
    st.subheader("📜 Execution Logs")
    with open("logs.txt", "r", encoding="utf-8") as f:
        st.code(f.read())


