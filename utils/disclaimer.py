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
    <div style="font-size: 13px; color: #9ca3af; text-align: center; margin-top: 10px; margin-bottom: 20px;">
        <em>Tariq, M. H. (2026). SIBO & IMO Prediction App (1.2). Zenodo. <br>
        <a href="https://doi.org/10.5281/zenodo.20032080" target="_blank" style="color: #60a5fa;">https://doi.org/10.5281/zenodo.20032080</a></em>
    </div>
    ''', unsafe_allow_html=True)
