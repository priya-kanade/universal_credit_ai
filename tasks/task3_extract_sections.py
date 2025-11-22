# tasks/task3_extract_sections.py

import json
import re

INPUT = "outputs/extracted_text.txt"
OUTPUT = "outputs/sections.json"

SECTIONS = {
    "definitions": [
        "means", "defined", "interpretation", "has the meaning"
    ],
    "obligations": [
        "must", "shall", "is required", "duty", "responsibility", "exercise"
    ],
    "responsibilities": [
        "must", "is required", "responsible", "duty"
    ],
    "eligibility": [
        "claimant", "eligible", "assessment", "limited capability", "entitled"
    ],
    "payments": [
        "amount", "increase", "rates", "CPI", "standard allowance", "LCWRA"
    ],
    "penalties": [
        "penalty", "sanction", "offence", "contravention"
    ],
    "record_keeping": [
        "report", "record", "must provide", "documentation", "information requirement"
    ]
}


def extract_matches(text, keywords):
    lines = text.split("\n")
    extracted = []

    for line in lines:
        if any(k in line.lower() for k in keywords):
            cleaned = re.sub(r"\s+", " ", line).strip()
            extracted.append(cleaned)

    if not extracted:
        return "Not specified in this Act."

    return extracted


def main():
    with open(INPUT, "r", encoding="utf-8") as f:
        text = f.read()

    results = {}

    for section, keywords in SECTIONS.items():
        results[section] = extract_matches(text, keywords)

    with open(OUTPUT, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    print(f"[Task-3] Extracted sections: {OUTPUT}")



if __name__ == "__main__":
    main()






