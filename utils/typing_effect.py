import streamlit as st
import time

def display_with_typing_effect(content, placeholder):
    """Display text with a typing animation effect"""
    full_response = ""
    for chunk in content.split():
        full_response += chunk + " "
        time.sleep(0.05)
        placeholder.markdown(full_response + "▌")
    placeholder.markdown(full_response)