import streamlit as st

def main():
    st.title("About HIV Chatbot")
    
    st.markdown("""
    ### Overview
    This HIV Chatbot is designed to provide accurate, reliable information about HIV/AIDS. 
    It uses advanced RAG (Retrieval-Augmented Generation) technology to ensure responses 
    are based on verified medical information.
    
    ### Features
    - 24/7 availability for HIV-related queries
    - Evidence-based responses
    - User-friendly interface
    - Confidential interactions
    
    ### Disclaimer
    This chatbot is for informational purposes only and should not replace professional medical advice.
    Always consult healthcare professionals for medical decisions.
    """)

if __name__ == "__main__":
    main()