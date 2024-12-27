import streamlit as st

def setup_navigation():
    # Custom CSS for enhanced navigation styling
    st.markdown("""
        <style>
        /* Navigation bar styling */
        header[data-testid="stHeader"] {
            background-color: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-bottom: 1px solid rgba(49, 51, 63, 0.2);
        }

        /* Navigation items styling */
        section[data-testid="stSidebar"] > div {
            padding-top: 2rem;
            background-color: #f8f9fa;
        }
        
        /* Sidebar navigation links */
        .css-1d391kg {
            padding: 1rem;
        }

        /* Active page indicator */
        .css-1d391kg.e1fqkh3o1 {
            background-color: #e6e9ef;
            border-radius: 4px;
        }

        /* Main content area */
        .main .block-container {
            padding-top: 2rem;
        }
        </style>
    """, unsafe_allow_html=True)
    
def setup_header():
    st.markdown("""
        <style>
        .main-header {
            font-size: 2.5rem;
            font-weight: 600;
            margin-bottom: 2rem;
            color: #1f2937;
        }
        
        .chat-message {
            padding: 1.25rem;
            border-radius: 0.75rem;
            margin: 1rem 0;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
        }
        
        .user-message {
            background-color: #f3f4f6;
            border-left: 4px solid #3b82f6;
        }
        
        .bot-message {
            background-color: #f8fafc;
            border-left: 4px solid #10b981;
        }

        /* Improved typography */
        h1, h2, h3 {
            color: #1f2937;
        }
        
        p {
            color: #374151;
            line-height: 1.6;
        }
        </style>
    """, unsafe_allow_html=True)

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