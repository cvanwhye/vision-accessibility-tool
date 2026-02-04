# 👁️ Multimodal Vision Agent

A powerful Streamlit application powered by **Google Gemini 2.5 Flash** for advanced image analysis. This tool provides automated image-to-text capabilities for accessibility, dataset annotation, and object detection.

## ✨ Features

- **Accessibility (Alt Text)**: Generates concise, descriptive alt text suitable for screen readers.
- **Detailed Scene Description**: Provides dense, detailed descriptions of image elements, including lighting, colors, and spatial relationships.
- **Object Detection (JSON)**: Identifies main objects in an image and returns them in a structured JSON format.

## 🛠️ Prerequisites

Before running the application, ensure you have the following installed:

- **Python 3.8+**
- A **Google Gemini API Key** (Get one at [Google AI Studio](https://aistudio.google.com/))

## 📦 Installation
1.  **Clone the repository** (if you haven't already):
    ```bash
    git clone <repository-url>
    cd vision-analyser
    ```

2.  **Install dependencies**:
    ```bash
    pip install streamlit google-generativeai python-dotenv pillow
    ```

3.  **Set up Environment Variables**:
    Create a `.env` file in the project root and add your API key:
    ```env
    GEMINI_API_KEY=your_actual_api_key_here
    ```

## 🚀 Usage

Run the application using Streamlit:

```bash
streamlit run vision.py
```

The application will open in your default web browser.

## 📂 Project Structure

- `vision.py`: The main application script containing the UI and logic.
- `.env`: Stores sensitive environment variables (API Key).
