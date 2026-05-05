import streamlit as st
import sys
import os
import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.styles import inject_custom_css, section_divider, get_diagnosis_badge, confidence_bar
from utils.disclaimer import show_disclaimer
from utils.model_utils import DIAGNOSIS_COLORS, get_clinical_interpretation
from utils.pdf_report import generate_pdf_report

st.set_page_config(page_title="Report Export | SIBO & IMO AI", layout="wide", initial_sidebar_state="expanded")
inject_custom_css()

with st.sidebar:
    st.markdown("### 🧬 SIBO & IMO AI")
    st.markdown("---")
    show_disclaimer()

# ===== HERO =====
st.markdown('''
<div class="hero-section animate-in">
    <div class="gradient-text gradient-text-lg">📄 Report Export</div>
    <div class="hero-subtitle">Preview and download a professional PDF diagnostic report</div>
</div>
''', unsafe_allow_html=True)

section_divider()

# Check for data
if 'current_patient' not in st.session_state or not st.session_state.current_patient:
    st.warning("⚠️ No prediction data found. Please go to the **Diagnosis** page and run a prediction first.")
    show_disclaimer()
    st.stop()

patient = st.session_state.current_patient
diagnosis = patient['diagnosis']
probabilities = patient['probabilities']
inputs = patient['inputs']
name = patient.get('name', 'N/A')
gender = patient.get('gender', 'N/A')

# ===== REPORT PREVIEW =====
st.markdown('<div class="gradient-text gradient-text-md">📋 Report Preview</div>', unsafe_allow_html=True)
st.markdown("")

# Patient info card
st.markdown(f'''
<div class="glass-card">
    <div style="font-size:18px; font-weight:700; color:#f1f5f9; margin-bottom:12px;">Patient Information</div>
    <div style="display:flex; gap:40px; color:#94a3b8;">
        <span><strong>Name:</strong> {name}</span>
        <span><strong>Age:</strong> {inputs.get("Age", "N/A")}</span>
        <span><strong>Gender:</strong> {gender}</span>
        <span><strong>Date:</strong> {datetime.datetime.now().strftime("%B %d, %Y")}</span>
    </div>
</div>
''', unsafe_allow_html=True)

# Test values card
st.markdown(f'''
<div class="glass-card">
    <div style="font-size:18px; font-weight:700; color:#f1f5f9; margin-bottom:12px;">Breath Test Values</div>
</div>
''', unsafe_allow_html=True)

val_cols = st.columns(4)
items = list(inputs.items())
for i, (key, val) in enumerate(items):
    with val_cols[i % 4]:
        display_key = key.replace('(ppm)', '').replace('(minutes)', '').strip()
        st.metric(label=display_key, value=f"{val:.1f}" if isinstance(val, float) else str(val))

section_divider()

# Diagnosis result card
badge = get_diagnosis_badge(diagnosis)
st.markdown(f'''
<div class="glass-card" style="text-align:center; padding:28px;">
    <div style="font-size:14px; color:#94a3b8; margin-bottom:10px; text-transform:uppercase; letter-spacing:1px;">
        Predicted Diagnosis
    </div>
    <div style="margin:12px 0;">{badge}</div>
</div>
''', unsafe_allow_html=True)

st.markdown("")
st.markdown("**Confidence Scores:**")
for cls in sorted(probabilities.keys(), key=lambda x: -probabilities[x]):
    color = DIAGNOSIS_COLORS.get(cls, '#6366f1')
    confidence_bar(cls, probabilities[cls], color)

section_divider()

# Clinical interpretation
st.markdown("**Clinical Interpretation:**")
interp = get_clinical_interpretation(diagnosis, inputs)
st.markdown(f'<div class="glass-card">{interp.replace(chr(10), "<br>")}</div>', unsafe_allow_html=True)

section_divider()

# ===== PDF DOWNLOAD =====
st.markdown('<div class="gradient-text gradient-text-md">⬇️ Download Report</div>', unsafe_allow_html=True)
st.markdown("")

col_dl1, col_dl2, col_dl3 = st.columns([1, 2, 1])
with col_dl2:
    try:
        pdf_bytes = generate_pdf_report(patient)
        filename = f"SIBO_IMO_Report_{name.replace(' ', '_')}_{datetime.datetime.now().strftime('%Y%m%d')}.pdf"
        st.download_button(
            label="📥 Download PDF Report",
            data=pdf_bytes,
            file_name=filename,
            mime="application/pdf",
            use_container_width=True,
        )
        st.caption("The PDF includes patient info, test values, prediction, confidence scores, and disclaimer.")
    except Exception as e:
        st.error(f"Error generating PDF: {e}")
        st.info("Make sure `fpdf2` is installed: `pip install fpdf2`")

section_divider()
show_disclaimer()
