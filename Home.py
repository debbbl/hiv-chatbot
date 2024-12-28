import streamlit as st
from ui_components import setup_navigation, setup_header

def main():
    # Set up page configuration and navigation
    st.set_page_config(
        page_title="HIV Information Assistant",
        page_icon="🏥",
        layout="wide"
    )
    setup_navigation()
    setup_header()

    st.image("images.jpg", width=300)
    
    st.title("Welcome to HIV Information Assistant")
    
    st.markdown("""
    ### Your Trusted Source for HIV Information
    
    Welcome to our HIV Information Assistant. This platform provides:
    
    - **Accurate Information**: Get reliable answers to your HIV-related questions
    - **24/7 Availability**: Access information whenever you need it
    - **Confidential**: Your queries are private and secure
    
    ### How to Use
    
    1. Navigate to the **Chatbot** section to start asking questions
    2. Explore the **About** section to learn more about this service
    3. Use the navigation menu at the top to switch between sections
    
    ### Getting Started
    
    Click on "Chatbot" in the navigation menu to begin your conversation.
    """)

    st.markdown("---")
    
    with st.expander("⚠️ Important Disclaimer"):
        st.markdown("""
        This chatbot provides general information about HIV/AIDS. It is not a substitute 
        for professional medical advice, diagnosis, or treatment. Always seek the advice 
        of your physician or other qualified health provider with questions about your 
        medical condition.
        """)

if __name__ == "__main__":
    main()