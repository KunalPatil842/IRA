import streamlit as st
import os
import textwrap
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()
api_key = os.getenv("GOOGLE_CLOUD_API_KEY")

# Configure the Gemini API
genai.configure(api_key=api_key)

def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

# Set page configuration
st.set_page_config(page_title="IRA", page_icon="images/AI.webp")

# Create a title and subtitle
st.title("IRA: Intelligent Response Assistant")
st.subheader("Ask me anything and get intelligent responses!")

# Create two columns for layout
col1, col2 = st.columns([1, 4])

# Add logo in the first column
with col1:
    st.image("images/AI.webp", width=100)

# Add input text area in the second column
with col2:
    input_text = st.text_area("Input your question:", height=100, placeholder="Type your question here...")

# Add a submit button
submit = st.button("Ask")

# Display the response when the button is clicked
if submit:
    if input_text.strip():  # Check if input is not empty
        response = get_gemini_response(input_text)
        st.subheader("Response:")
        st.write(response)
    else:
        st.warning("Please enter a question before submitting.")

# Add some footer information
st.markdown("---")
st.markdown("Made with ❤️ by Batch 21 ZOOTOPIA Team")