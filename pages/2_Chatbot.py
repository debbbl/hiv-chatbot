import streamlit as st
from chatbot import Chatbot
from ui_components import display_chat_message, display_follow_up_questions
from chat_handler import process_query

def initialize_chat_state():
    if 'chatbot' not in st.session_state:
        st.session_state.chatbot = Chatbot()
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    if 'current_follow_up_questions' not in st.session_state:
        st.session_state.current_follow_up_questions = []

def display_chat_interface():
    st.title("🤖 HIV Chatbot")
    st.markdown("""
    Welcome to the HIV Information Chatbot. Ask any questions about HIV, and I'll provide 
    accurate, supportive information based on reliable sources.
    """)
    
    for message in st.session_state.chat_history:
        display_chat_message(message["role"], message["content"])

    clicked_question = display_follow_up_questions(st.session_state.current_follow_up_questions)
    query = st.chat_input("Type your question here...")

    if query or clicked_question:
        selected_query = query or clicked_question
        process_query(selected_query, st.session_state.chatbot)
        st.rerun()

def main():
    try:
        initialize_chat_state()
        display_chat_interface()
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()