import streamlit as st
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.styles import inject_custom_css, section_divider, get_diagnosis_badge, confidence_bar
from utils.disclaimer import show_disclaimer
from utils.model_utils import (
    predict_diagnosis, store_patient_in_session,
    add_patient_to_comparison, DIAGNOSIS_COLORS,
)

st.set_page_config(page_title="Diagnosis | SIBO & IMO AI", layout="wide", initial_sidebar_state="expanded")
inject_custom_css()

# ===== SIDEBAR =====
with st.sidebar:
    st.markdown("### 🧬 SIBO & IMO AI")
    st.markdown("---")
    st.markdown("**Navigation**")
    st.caption("Use the sidebar to switch between pages.")
    st.markdown("---")
    show_disclaimer()

# ===== HERO =====
st.markdown('''
<div class="hero-section animate-in">
    <div class="gradient-text gradient-text-lg">🔬 Patient Diagnosis</div>
    <div class="hero-subtitle">Enter breath test values to receive an AI-powered prediction</div>
</div>
''', unsafe_allow_html=True)

section_divider()

# ===== PATIENT INFO =====
st.markdown('<div class="gradient-text gradient-text-md">📋 Patient Information</div>', unsafe_allow_html=True)
st.markdown("")

col_info1, col_info2, col_info3 = st.columns(3)
with col_info1:
    patient_name = st.text_input("Patient Name", value="", placeholder="Enter patient name")
with col_info2:
    age = st.number_input("Age", min_value=0, max_value=120, value=30, step=1)
with col_info3:
    gender = st.selectbox("Gender", options=["Male", "Female"])

section_divider()

# ===== BREATH TEST INPUTS =====
st.markdown('<div class="gradient-text gradient-text-md">🫁 Breath Test Values</div>', unsafe_allow_html=True)
st.markdown("")

col1, col2 = st.columns(2)

with col1:
    baseline_h2 = st.number_input("Baseline H₂ (ppm)", min_value=0.0, value=5.0, step=0.1)
    baseline_ch4 = st.number_input("Baseline CH₄ (ppm)", min_value=0.0, value=2.0, step=0.1)
    combined_peak = st.number_input("Combined Peak (ppm)", min_value=0.0, value=95.0, step=0.1)

with col2:
    peak_h2 = st.number_input("Peak H₂ (ppm)", min_value=0.0, value=74.0, step=0.1)
    peak_ch4 = st.number_input("Peak CH₄ (ppm)", min_value=0.0, value=21.0, step=0.1)
    time_of_peak = st.number_input("Time of Peak (minutes)", min_value=0.0, value=100.0, step=1.0)

increase_from_baseline = st.number_input("Increase from Baseline (ppm)", min_value=0.0, value=90.0, step=0.1)

section_divider()

# ===== PREDICT BUTTON =====
col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
with col_btn2:
    predict_clicked = st.button("🧬 Predict Diagnosis", use_container_width=True)

if predict_clicked:
    with st.spinner("🔄 Analysing breath test data..."):
        diagnosis, probabilities, input_df = predict_diagnosis(
            age, baseline_h2, baseline_ch4, peak_h2, peak_ch4,
            combined_peak, time_of_peak, increase_from_baseline
        )

    # Store in session for other pages
    input_values = {
        'Age': age,
        'Baseline H₂ (ppm)': baseline_h2,
        'Baseline CH₄ (ppm)': baseline_ch4,
        'Peak H₂ (ppm)': peak_h2,
        'Peak CH₄ (ppm)': peak_ch4,
        'Combined Peak (ppm)': combined_peak,
        'Time of Peak (minutes)': time_of_peak,
        'Increase from Baseline (ppm)': increase_from_baseline,
    }
    store_patient_in_session(patient_name, gender, input_values, diagnosis, probabilities)

    section_divider()

    # ===== RESULTS =====
    st.markdown('<div class="gradient-text gradient-text-md">📊 Prediction Results</div>', unsafe_allow_html=True)
    st.markdown("")

    # Diagnosis badge
    badge_html = get_diagnosis_badge(diagnosis)
    st.markdown(f'''
    <div class="glass-card animate-in" style="text-align:center; padding:30px;">
        <div style="font-size:14px; color:#94a3b8; margin-bottom:12px; text-transform:uppercase; letter-spacing:1px;">
            Predicted Diagnosis
        </div>
        <div style="margin:16px 0;">{badge_html}</div>
        <div style="font-size:13px; color:#64748b; margin-top:12px;">
            Patient: {patient_name or "Not specified"} | Age: {age} | Gender: {gender}
        </div>
    </div>
    ''', unsafe_allow_html=True)

    st.markdown("")

    # Confidence bars
    st.markdown("**Confidence Scores**")
    for cls in sorted(probabilities.keys(), key=lambda x: -probabilities[x]):
        color = DIAGNOSIS_COLORS.get(cls, '#6366f1')
        confidence_bar(cls, probabilities[cls], color)

    st.markdown("")

    # Quick summary
    max_class = max(probabilities, key=probabilities.get)
    max_pct = probabilities[max_class]
    st.markdown(f'''
    <div class="glass-card">
        <div style="font-size:14px; color:#94a3b8;">Quick Summary</div>
        <div style="margin-top:8px; font-size:15px;">
            The model predicts <strong>{diagnosis}</strong> with <strong>{max_pct:.1f}%</strong> confidence.
            Navigate to <strong>AI Insights</strong> for a detailed clinical interpretation,
            or <strong>Report Export</strong> to download a PDF report.
        </div>
    </div>
    ''', unsafe_allow_html=True)

    # Option to add to comparison
    st.markdown("")
    if st.button("➕ Add this patient to Comparison List"):
        add_patient_to_comparison(st.session_state.current_patient.copy())
        count = len(st.session_state.patients_list)
        st.success(f"✅ Patient added! ({count} patient(s) in comparison list)")

section_divider()
show_disclaimer()
