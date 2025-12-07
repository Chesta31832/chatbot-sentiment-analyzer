import streamlit as st
from src.sentiment_analyzer import SentimentAnalyzer
from src.chatbot import Chatbot

# Page configuration
st.set_page_config(page_title="Sentiment Analysis Chatbot", page_icon="🤖")

# Initialize classes
if 'analyzer' not in st.session_state:
    st.session_state.analyzer = SentimentAnalyzer()
if 'chatbot' not in st.session_state:
    st.session_state.chatbot = Chatbot()
if 'messages' not in st.session_state:
    st.session_state.messages = []

st.title("🤖 Sentiment Analysis Chatbot")
st.markdown("Chat with me! I'll analyze the sentiment of your messages in real-time.")

# Sidebar for stats
with st.sidebar:
    st.header("Conversation Stats")
    if st.button("Clear Conversation"):
        st.session_state.messages = []
        st.rerun()

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if "sentiment" in message:
            st.caption(f"Sentiment: {message['sentiment']}")

# Chat input
if prompt := st.chat_input("What is on your mind?"):
    # User message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Analyze
    scores, label = st.session_state.analyzer.analyze_with_label(prompt)
    
    # Bot response
    # Note: We are passing the label to get_response. 
    # If you updated chatbot.py to take score, we could pass scores['compound'] too.
    response = st.session_state.chatbot.get_response(prompt, label)
    
    # Display Bot message
    with st.chat_message("assistant"):
        st.markdown(response)
        
        # Color-coded sentiment indicator
        color = "gray"
        if label == "Positive":
            color = "green"
        elif label == "Negative":
            color = "red"
        else:
            color = "orange"
            
        st.markdown(f":{color}[Detected Sentiment: **{label}** (Score: {scores['compound']:.2f})]")

    # Save bot message with sentiment info for history
    st.session_state.messages.append({
        "role": "assistant", 
        "content": response,
        "sentiment": f"{label} ({scores['compound']:.2f})"
    })
