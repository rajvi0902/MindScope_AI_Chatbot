# app.py

import streamlit as st
from dotenv import load_dotenv
import os
from langchain.llms import GooglePalm
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_google_genai import ChatGoogleGenerativeAI
from htmlTemplate import bot_template, user_template, css
from langchain.prompts import PromptTemplate

load_dotenv()

st.set_page_config(page_title="MindScope AI Chatbot", layout="wide")
st.markdown(css, unsafe_allow_html=True)

# Initialize chat history if not present
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Load Gemini API Key
api_key = os.getenv("GOOGLE_API_KEY")
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
memory = ConversationBufferMemory()
conversation = ConversationChain(llm=llm, memory=memory)

# Display existing chat history
for chat in st.session_state.chat_history:
    if chat['role'] == 'user':
        st.markdown(user_template.replace("{{MSG}}", chat['content']), unsafe_allow_html=True)
    else:
        st.markdown(bot_template.replace("{{MSG}}", chat['content']), unsafe_allow_html=True)

# Input & send button layout (bottom center)
st.markdown("""
    <style>
    .input-container {
        display: flex;
        justify-content: center;
        align-items: center;
        position: fixed;
        bottom: 20px;
        left: 50%;
        transform: translateX(-50%);
        width: 60%;
        z-index: 100;
    }
    .input-box {
        width: 100%;
        display: flex;
        background-color: #1e1e1e;
        border-radius: 12px;
        overflow: hidden;
    }
    .input-box textarea {
        flex: 1;
        padding: 1rem;
        font-size: 1rem;
        border: none;
        resize: none;
        color: white;
        background: #1e1e1e;
    }
    .input-box button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 1rem 1.5rem;
        cursor: pointer;
    }
    </style>
""", unsafe_allow_html=True)

prompt = st.text_area("", placeholder="Type your message here...", key="user_input")
send = st.button("Send", use_container_width=True)

# On submit
if send and prompt:
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    response = conversation.predict(input=prompt)
    st.session_state.chat_history.append({"role": "bot", "content": response})
    st.rerun()
