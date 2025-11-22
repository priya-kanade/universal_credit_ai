import pdfplumber
import os
import re
import hashlib
from pathlib import Path

PDF_PATH = "Universal_Credit_Act_2025.pdf"
OUTPUT_PATH = "outputs/extracted_text.txt"


def clean_text(text: str):
    # Remove large whitespace blocks
    text = re.sub(r"[ \t]+", " ", text)

    # Remove duplicate blank lines
    text = re.sub(r"\n{2,}", "\n\n", text)

    # Remove common headers like "Universal Credit Act 2025"
    text = re.sub(r"Universal Credit Act.*?\n", "", text, flags=re.IGNORECASE)

    return text.strip()


def extract_and_clean(pdf_path, output_path):
    os.makedirs("outputs", exist_ok=True)

    final_pages = []
    seen_hashes = set()

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            raw = page.extract_text() or ""
            cleaned = clean_text(raw)

            # Remove repeated pages using checksum
            page_hash = hashlib.md5(cleaned.encode()).hexdigest()
            if page_hash not in seen_hashes:
                final_pages.append(cleaned)
                seen_hashes.add(page_hash)

    full_text = "\n\n".join(final_pages)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(full_text)

    print(f"[Task-1] Extracted and cleaned {len(final_pages)} pages → {output_path}")


if __name__ == "__main__":
    extract_and_clean(PDF_PATH, OUTPUT_PATH)


