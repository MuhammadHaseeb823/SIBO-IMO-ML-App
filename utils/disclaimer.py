import streamlit as st


def show_disclaimer():
    """Display the educational-use disclaimer on every page."""
    st.markdown('''
    <div class="disclaimer-bar">
        ⚠️ <strong>Disclaimer:</strong> This application is strictly for educational purposes only
        and should not be used as a substitute for professional medical advice, diagnosis, or treatment.
        Always seek the advice of a qualified healthcare provider with any questions you may have
        regarding a medical condition.
    </div>
    ''', unsafe_allow_html=True)
