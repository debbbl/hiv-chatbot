import streamlit as st
import pandas as pd

def main():
    st.title("About HIV Chatbot")
    
    st.markdown("""
    ### Overview
    The HIV Chatbot is a cutting-edge tool designed to provide accurate, reliable, and evidence-based information about HIV/AIDS. 
    Leveraging advanced artificial intelligence, it ensures that responses are informative and aligned with trusted medical guidelines.

    ### How It Works
    The chatbot uses a **Retrieval-Augmented Generation (RAG)** approach:
    - **Retrieval**: Questions are matched against a curated HIV Q&A database, created using information from:
        - The World Health Organization (WHO)
        - HIV Testing Guidelines by the Malaysian Society for HIV Medicine
    - **Generation**: Responses are generated using a powerful language model, **LLaMA3-8B**, ensuring conversational and contextually relevant answers.

    ### Model Performance
    Below are key evaluation metrics for the chatbot:
    - **Accuracy**: 0.8667
    - **F1 Score**: 0.9286
    - **Average Response Time**: 2.5155 seconds
    - **Cosine Similarity**: 0.8325
    - **ROUGE-L Score**: 0.5035
    
    These metrics demonstrate the model's ability to provide precise, context-aware responses efficiently.
    """)
    
    st.markdown("""
    ### Features
    - **24/7 Availability**: Always ready to assist with HIV-related questions.
    - **Evidence-Based Responses**: Backed by trusted sources and medical guidelines.
    - **User-Friendly Interface**: Easy navigation and accessibility for all users.
    - **Confidential Interactions**: Ensures user privacy and data security.

    ### Disclaimer
    This chatbot is for informational purposes only and should not replace professional medical advice. 
    Always consult healthcare professionals for medical decisions.

    ### Acknowledgments
    - **Data Sources**: World Health Organization (WHO), Malaysian Society for HIV Medicine.
    - **Technology**: Built with Retrieval-Augmented Generation (RAG) and powered by LLaMA3-8B.
    - **Evaluation Tools**: Metrics like accuracy, F1 score, and ROUGE-L used to assess performance.

    """)

if __name__ == "__main__":
    main()
