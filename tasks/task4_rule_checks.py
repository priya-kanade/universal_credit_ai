# tasks/task4_rule_checks.py
import json

INPUT = "outputs/sections.json"
OUTPUT = "outputs/rules.json"

RULES = [
    {
        "name": "Act must define key terms",
        "key": "definitions"
    },
    {
        "name": "Act must specify eligibility criteria",
        "key": "eligibility"
    },
    {
        "name": "Act must specify responsibilities of the administering authority",
        "key": "responsibilities"
    },
    {
        "name": "Act must include enforcement or penalties",
        "key": "penalties"
    },
    {
        "name": "Act must include payment calculation or entitlement structure",
        "key": "payments"
    },
    {
        "name": "Act must include record-keeping or reporting requirements",
        "key": "record_keeping"
    }
]


def evaluate_rule(section_content):
    """
    Accepts a section value from Task-3.
    If it's a list and not empty → pass
    If it's a string saying “Not specified …” → fail
    """
    if isinstance(section_content, list) and len(section_content) > 0:
        return "pass", section_content[0]
    if isinstance(section_content, str) and "not" in section_content.lower():
        return "fail", section_content
    return "fail", "No supporting evidence found."


def main():
    with open(INPUT, "r", encoding="utf-8") as f:
        sections = json.load(f)

    results = []

    for rule in RULES:
        data = sections.get(rule["key"], "")
        status, evidence = evaluate_rule(data)

        # Confidence is just heuristic
        confidence = 95 if status == "pass" else 60

        results.append({
            "rule": rule["name"],
            "status": status,
            "evidence": evidence,
            "confidence": confidence
        })

    with open(OUTPUT, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    print(f"[Task-4] Rule evaluation completed: {OUTPUT}")



if __name__ == "__main__":
    main()


