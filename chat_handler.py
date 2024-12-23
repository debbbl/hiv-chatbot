import streamlit as st
from utils.typing_effect import display_with_typing_effect

def add_to_chat_history(role, content):
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    st.session_state.chat_history.append({"role": role, "content": content})

def display_message(role, content):
    """Display a chat message with typing effect for assistant"""
    with st.chat_message(role):
        if role == "assistant":
            placeholder = st.empty()
            display_with_typing_effect(content, placeholder)
        else:
            st.write(content)

def process_query(query, chatbot):
    display_message("user", query)
    add_to_chat_history("user", query)
    
    response = chatbot.generate_response(query)
    display_message("assistant", response)
    add_to_chat_history("assistant", response)
    
    follow_up_questions = chatbot.generate_follow_up_questions(query)
    st.session_state.current_follow_up_questions = follow_up_questions