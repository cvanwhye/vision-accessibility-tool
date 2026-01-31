import streamlit as st
import google.generativeai as genai
import os
from PIL import Image
from dotenv import load_dotenv

# 1. Load Credentials
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

st.set_page_config(page_title="Multimodal Vision Agent", layout="centered")

# --- Logic: The Vision Engine ---
def analyze_image(image_file, prompt_type, key):
    try:
        genai.configure(api_key=key)
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        # Open the image with PIL (Python Imaging Library)
        img = Image.open(image_file)
        
        # Switch prompts based on user goal
        if prompt_type == "Accessibility (Alt Text)":
            prompt = """
            You are an Accessibility Expert.
            Write a concise, descriptive 'Alt Text' for this image for a screen reader.
            Focus on the main subject and action. No flowery language.
            Format: "Alt Text: [description]"
            """
        elif prompt_type == "Detailed Scene Description":
            prompt = """
            You are a Computer Vision Dataset Annotator.
            Provide a dense, detailed description of every element in the image.
            Include: Lighting, colors, spatial relationships (left/right/background), and text if visible.
            """
        else: # Object Detection (JSON)
            prompt = """
            List the main objects visible in the image in JSON format.
            Return a list of strings: ["Object 1", "Object 2", ...]
            """
        
        # The Magic Line: We pass the prompt AND the image to the model
        with st.spinner("Analyzing pixels..."):
            response = model.generate_content([prompt, img])
            return response.text
            
    except Exception as e:
        return f"Error: {e}"

# --- UI Layout ---
st.title("👁️ AI Vision Analyst")
st.markdown("Automated **Image-to-Text** for Dataset Annotation & Accessibility.")

# 1. Upload
uploaded_file = st.file_uploader("Upload an Image (JPG/PNG)", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Show the image
    st.image(uploaded_file, caption="Input Image")
    
    st.divider()
    
    # 2. Select Task
    task = st.radio("Select Analysis Task:", 
                    ["Accessibility (Alt Text)", 
                     "Detailed Scene Description", 
                     "Object Detection (JSON)"], 
                    horizontal=True)
    
    # 3. Analyze
    if st.button("🚀 Analyze Image"):
        if not api_key:
            st.error("Missing API Key.")
        else:
            result = analyze_image(uploaded_file, task, api_key)
            st.success("Analysis Complete")
            st.code(result, language="json" if "JSON" in task else "markdown")