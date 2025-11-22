import os
import json
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


INPUT = "outputs/extracted_text.txt"
OUTPUT = "outputs/summary_ai.json"

MODEL = "facebook/bart-large-cnn"


def split_into_chunks(text, max_tokens=1024):
    """
    Split clean text into reasonable chunks without breaking sentences mid-way.
    """
    sentences = text.split(".")
    chunks = []
    current = ""

    for sent in sentences:
        sent = sent.strip()
        if not sent:
            continue

        if len(current) + len(sent) < max_tokens:
            current += sent + ". "
        else:
            chunks.append(current.strip())
            current = sent + ". "

    if current.strip():
        chunks.append(current.strip())

    return chunks


def summarize_chunks(chunks, tokenizer, model, device):
    bullet_results = []

    for i, chunk in enumerate(chunks):
        print(f"[Task-2] Summarizing chunk {i+1}/{len(chunks)}...")

        prompt = (
            "Summarize the following UK Act text into concise bullet points "
            "covering: Purpose, Key Definitions, Eligibility (if any), "
            "Obligations, Enforcement, and Financial/Payment Details:\n\n"
            + chunk
        )

        inputs = tokenizer(
            prompt,
            return_tensors="pt",
            truncation=True,
            max_length=1024
        ).to(device)

        output = model.generate(
            **inputs,
            max_new_tokens=256,
            num_beams=4,
            early_stopping=True
        )

        summary = tokenizer.decode(output[0], skip_special_tokens=True)
        bullet_results.append(summary)

    return bullet_results


def merge_and_deduplicate(bullet_points):
    combined = "\n".join(bullet_points)
    lines = set()

    cleaned = []
    for line in combined.split("\n"):
        line = line.strip(" -•\t")
        if line and line.lower() not in lines:
            lines.add(line.lower())
            cleaned.append(line)

    # Limit to max 12 bullets
    return cleaned[:12]


def main():
    os.makedirs("outputs", exist_ok=True)

    with open(INPUT, "r", encoding="utf-8") as f:
        text = f.read().strip()

    if not text:
        raise SystemExit("❌ No text found. Run Task-1 first.")

    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"[Task-2] Loading model on {device.upper()}...")

    tokenizer = AutoTokenizer.from_pretrained(MODEL)
    model = AutoModelForSeq2SeqLM.from_pretrained(MODEL).to(device)

    chunks = split_into_chunks(text)
    print(f"[Task-2] Document split into {len(chunks)} chunks")

    chunk_summaries = summarize_chunks(chunks, tokenizer, model, device)
    final_summary = merge_and_deduplicate(chunk_summaries)

    with open(OUTPUT, "w", encoding="utf-8") as f:
        json.dump(final_summary, f, indent=2)

    print(f"[Task-2] Final AI summary saved → {OUTPUT}\n")
    print("\n".join(f"• {p}" for p in final_summary))


if __name__ == "__main__":
    main()
