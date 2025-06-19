import streamlit as st
import requests

# Sidebar: Choose model name
st.sidebar.title("LLM Settings")
model_name = st.sidebar.text_input("Ollama Model Name", value="gemma:3b")

# App title
st.title("🧠 Chat with Ollama LLMs")
st.write(f"Currently using model: `{model_name}`")

# Text input
user_prompt = st.text_area("Enter your prompt", height=150)

if st.button("Submit"):
    if not user_prompt.strip():
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Thinking..."):
            try:
                response = requests.post(
                    "http://localhost:11434/api/generate",
                    json={"model": model_name, "prompt": user_prompt, "stream": False}
                )
                response.raise_for_status()
                result = response.json()
                st.success("Response:")
                st.write(result.get("response", "No response found."))
            except requests.exceptions.RequestException as e:
                st.error(f"Error: {e}")
