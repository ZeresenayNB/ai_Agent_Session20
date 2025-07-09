import streamlit as st
from utils.pdf_utils import extract_text_from_pdf
from utils.ai_utils import analyze_symptoms
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Streamlit Page Config
st.set_page_config(page_title="🩺 AI Medical Assistant", layout="centered")

st.title("🩺 AI Medical Assistant")
st.markdown("""
Upload a **PDF** file describing your symptoms. The AI assistant will:
- Extract and summarize your symptoms
- Suggest possible causes
- Recommend treatments and medications

> ⚠️ **Note:** This is not a substitute for professional medical advice.
""")

# OpenAI API Key Input
api_key = st.text_input("🔑 Enter your OpenAI API Key", type="password")
if not api_key:
    st.info("🔐 Your key is not stored anywhere. Used only for this session.")

# PDF Upload
uploaded_file = st.file_uploader("📄 Upload your symptoms (PDF)", type=["pdf"])

# Process PDF and Analyze
if uploaded_file and api_key:
    with st.spinner("📖 Reading PDF..."):
        pdf_text = extract_text_from_pdf(uploaded_file)

    st.subheader("📋 Extracted Text")
    st.text_area("Content", pdf_text, height=200)

    if st.button("🧠 Analyze Symptoms"):
        with st.spinner("🤖 Analyzing..."):
            result = analyze_symptoms(pdf_text, api_key)

        st.subheader("📊 AI Medical Report")

        st.markdown("### 📝 Symptom Summary")
        st.write(result.get("summary", "Not available"))

        st.markdown("### 🦠 Possible Causes")
        st.write(result.get("causes", "Not available"))

        st.markdown("### 💊 Suggested Treatments")
        st.write(result.get("treatments", "Not available"))

        st.markdown("### 🧪 Medication Recommendations")
        st.write(result.get("medications", "Not available"))

# Footer Instructions
st.markdown("---")
st.markdown("""
### 🚀 How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
""")