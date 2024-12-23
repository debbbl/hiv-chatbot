import streamlit as st

def setup_navigation():
    with st.sidebar:
        st.title("Navigation")
        page = st.radio(
            "Go to:",
            options=["🏠 Home", "💬 Chat", "ℹ️ About"]
        )
        
        st.divider()
        st.markdown("### About this Chatbot")
        st.markdown("""
        This chatbot provides accurate, supportive information 
        about HIV using reliable medical sources.
        """)

def setup_header():
    st.title("🤖 HIV Chatbot")
    st.markdown("""
    Welcome to the HIV Information Chatbot. Ask any questions about HIV, and I'll provide 
    accurate, supportive information based on reliable sources.
    """)

def display_chat_message(role, content):
    with st.chat_message(role):
        st.write(content)

def display_follow_up_questions(questions):
    if not questions:
        return None
        
    st.markdown("<br>", unsafe_allow_html=True)
    
    with st.container():
        st.markdown("### **You might want to ask:**")
        cols = st.columns(len(questions))
        for i, (col, question) in enumerate(zip(cols, questions)):
            with col:
                if st.button(f"{question}", key=f"follow_up_{i}_{hash(question)}"):
                    return question
    return None