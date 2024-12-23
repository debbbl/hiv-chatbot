import streamlit as st
from chatbot import Chatbot
from ui_components import (
    setup_navigation, 
    setup_header, 
    display_chat_message, 
    display_follow_up_questions
)
from chat_handler import process_query

def setup_ui():
    st.set_page_config(page_title="HIV Chatbot", layout="wide")
    setup_navigation()
    setup_header()

def initialize_session_state():
    if 'chatbot' not in st.session_state:
        st.session_state.chatbot = Chatbot()
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    if 'current_follow_up_questions' not in st.session_state:
        st.session_state.current_follow_up_questions = []

def display_chat_history():
    for message in st.session_state.chat_history:
        display_chat_message(message["role"], message["content"])

def handle_user_interaction():
    clicked_question = display_follow_up_questions(st.session_state.current_follow_up_questions)

    query = st.chat_input("Type your question here...")

    if query or clicked_question:
        selected_query = query or clicked_question
        process_query(selected_query, st.session_state.chatbot)
        st.rerun() 

def main():
    try:
        setup_ui()
        initialize_session_state()
        display_chat_history()
        handle_user_interaction()
        
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        st.error("Please make sure all required files are present and the API key is set correctly.")

if __name__ == "__main__":
    main()