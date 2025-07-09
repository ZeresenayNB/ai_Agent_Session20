import openai

def analyze_symptoms(text: str, api_key: str) -> dict:
    openai.api_key = api_key

    prompt = f"""
You are a medical assistant AI. A user has provided the following symptoms:

\"\"\"
{text}
\"\"\"

1. Summarize the symptoms.
2. Suggest the most likely causes or conditions.
3. Recommend general treatments (non-specific to individuals).
4. Recommend general medications (with standard usage).

Respond clearly and concisely.
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=800
    )

    reply = response["choices"][0]["message"]["content"]

    # Optional: Parse the reply if it follows structure
    sections = {"summary": "", "causes": "", "treatments": "", "medications": ""}
    lines = reply.split("\n")
    current_section = None
    for line in lines:
        if "summarize" in line.lower():
            current_section = "summary"
        elif "causes" in line.lower():
            current_section = "causes"
        elif "treatments" in line.lower():
            current_section = "treatments"
        elif "medications" in line.lower():
            current_section = "medications"
        elif current_section:
            sections[current_section] += line.strip() + "\n"

    return sections

