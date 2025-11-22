import streamlit as st
import requests

EURI_API_KEY = "Put_your_euri_API_key_here"

API_URL = "https://api.euron.one/api/v1/euri/chat/completions"

HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {EURI_API_KEY}"
}

def get_sentiment_from_euri(text):
    prompt = f"Analyze the sentiment of the following text and return one of the following: Positive, Negative, Neutral, Political, Racist. Text:\"{text}"
    
    payload = {
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "model": "gpt-4.1-nano",
        "max_tokens": 100,
        "temperature": 0.3
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload)

    if response.status_code == 200:
        reply = response.json()["choices"][0]["message"]["content"]
        return reply.strip()
    else:
        return f"Error: {response.status_code} - {response.text}"
    
st.set_page_config(page_title="Real-Time Sentiment Analyzer", layout="centered")
st.title("Real-Time Sentiment Analyzer")
st.markdown("Enter a sentence or social media post to analyze its sentiment.")

user_input = st.text_area("Enter your text here:", height=150)

if st.button("Analyze Sentiment"):
    if user_input.lower().strip():
        with st.spinner("Analyzing..."):
            result = get_sentiment_from_euri(user_input)
            st.success(f"Sentiment: {result}")
    else:
        st.warning("Please enter valid text.")