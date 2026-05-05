import streamlit as st
import sys
import os
import pandas as pd
import plotly.graph_objects as go

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.styles import inject_custom_css, section_divider, get_diagnosis_badge
from utils.disclaimer import show_disclaimer
from utils.model_utils import (
    predict_diagnosis, add_patient_to_comparison,
    DIAGNOSIS_COLORS, FEATURE_NAMES,
)

st.set_page_config(page_title="Patient Comparison | SIBO & IMO AI", layout="wide", initial_sidebar_state="expanded")
inject_custom_css()

with st.sidebar:
    st.markdown("### 🧬 SIBO & IMO AI")
    st.markdown("---")
    show_disclaimer()

# ===== HERO =====
st.markdown('''
<div class="hero-section animate-in">
    <div class="gradient-text gradient-text-lg">👥 Patient Comparison</div>
    <div class="hero-subtitle">Compare breath test results and predictions across multiple patients</div>
</div>
''', unsafe_allow_html=True)

section_divider()

# Initialise session state
if 'patients_list' not in st.session_state:
    st.session_state.patients_list = []

# ===== ADD PATIENT FORM =====
st.markdown('<div class="gradient-text gradient-text-md">➕ Add a Patient</div>', unsafe_allow_html=True)
st.markdown("")

with st.form("add_patient_form", clear_on_submit=True):
    fc1, fc2, fc3 = st.columns(3)
    with fc1:
        p_name = st.text_input("Patient Name", placeholder="e.g. Patient A")
    with fc2:
        p_age = st.number_input("Age", min_value=0, max_value=120, value=30, step=1, key="comp_age")
    with fc3:
        p_gender = st.selectbox("Gender", ["Male", "Female"], key="comp_gender")

    fc4, fc5 = st.columns(2)
    with fc4:
        p_bh2 = st.number_input("Baseline H₂ (ppm)", min_value=0.0, value=5.0, step=0.1, key="comp_bh2")
        p_bch4 = st.number_input("Baseline CH₄ (ppm)", min_value=0.0, value=2.0, step=0.1, key="comp_bch4")
        p_comb = st.number_input("Combined Peak (ppm)", min_value=0.0, value=95.0, step=0.1, key="comp_comb")
    with fc5:
        p_ph2 = st.number_input("Peak H₂ (ppm)", min_value=0.0, value=74.0, step=0.1, key="comp_ph2")
        p_pch4 = st.number_input("Peak CH₄ (ppm)", min_value=0.0, value=21.0, step=0.1, key="comp_pch4")
        p_time = st.number_input("Time of Peak (min)", min_value=0.0, value=100.0, step=1.0, key="comp_time")

    p_inc = st.number_input("Increase from Baseline (ppm)", min_value=0.0, value=90.0, step=0.1, key="comp_inc")

    submitted = st.form_submit_button("🧬 Add & Predict", use_container_width=True)

    if submitted:
        diagnosis, probs, _ = predict_diagnosis(
            p_age, p_bh2, p_bch4, p_ph2, p_pch4, p_comb, p_time, p_inc
        )
        patient_data = {
            'name': p_name or f"Patient {len(st.session_state.patients_list) + 1}",
            'gender': p_gender,
            'inputs': {
                'Age': p_age, 'Baseline H₂ (ppm)': p_bh2, 'Baseline CH₄ (ppm)': p_bch4,
                'Peak H₂ (ppm)': p_ph2, 'Peak CH₄ (ppm)': p_pch4,
                'Combined Peak (ppm)': p_comb, 'Time of Peak (minutes)': p_time,
                'Increase from Baseline (ppm)': p_inc,
            },
            'diagnosis': diagnosis,
            'probabilities': probs,
        }
        add_patient_to_comparison(patient_data)
        st.success(f"✅ Added **{patient_data['name']}** — Diagnosis: **{diagnosis}**")

section_divider()

# ===== COMPARISON TABLE =====
patients = st.session_state.patients_list

if not patients:
    st.info("No patients added yet. Use the form above or add patients from the Diagnosis page.")
    show_disclaimer()
    st.stop()

st.markdown(f'<div class="gradient-text gradient-text-md">📋 Comparison Table ({len(patients)} patients)</div>',
            unsafe_allow_html=True)
st.markdown("")

# Build comparison dataframe
rows = []
for p in patients:
    row = {'Name': p['name'], 'Gender': p['gender'], 'Diagnosis': p['diagnosis']}
    row.update(p['inputs'])
    conf = max(p['probabilities'].values())
    row['Confidence'] = f"{conf:.1f}%"
    rows.append(row)

df_comp = pd.DataFrame(rows)
st.dataframe(df_comp, use_container_width=True, hide_index=True)

section_divider()

# ===== COMPARISON CHART =====
st.markdown('<div class="gradient-text gradient-text-md">📊 Gas Levels Comparison</div>', unsafe_allow_html=True)
st.markdown("")

chart_features = ['Baseline H₂ (ppm)', 'Baseline CH₄ (ppm)', 'Peak H₂ (ppm)',
                  'Peak CH₄ (ppm)', 'Combined Peak (ppm)', 'Increase from Baseline (ppm)']

colors_list = ['#38bdf8', '#a78bfa', '#f59e0b', '#ef4444', '#22c55e', '#6366f1', '#ec4899', '#14b8a6']

fig = go.Figure()
for i, p in enumerate(patients):
    vals = [p['inputs'].get(f, 0) for f in chart_features]
    labels = [f.replace(' (ppm)', '') for f in chart_features]
    fig.add_trace(go.Bar(
        name=p['name'],
        x=labels,
        y=vals,
        marker_color=colors_list[i % len(colors_list)],
    ))

fig.update_layout(
    barmode='group',
    template='plotly_dark',
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    height=420,
    margin=dict(l=10, r=10, t=10, b=10),
    font=dict(family='Inter', color='#94a3b8'),
    legend=dict(orientation='h', y=-0.15),
    yaxis_title='ppm',
)
st.plotly_chart(fig, use_container_width=True)

section_divider()

# ===== DIAGNOSIS MATRIX =====
st.markdown('<div class="gradient-text gradient-text-md">🎯 Diagnosis Overview</div>', unsafe_allow_html=True)
st.markdown("")

diag_cols = st.columns(min(len(patients), 4))
for i, p in enumerate(patients):
    with diag_cols[i % 4]:
        badge = get_diagnosis_badge(p['diagnosis'])
        conf = max(p['probabilities'].values())
        st.markdown(f'''
        <div class="glass-card" style="text-align:center; padding:20px;">
            <div style="font-weight:600; color:#e2e8f0; margin-bottom:8px;">{p["name"]}</div>
            {badge}
            <div style="font-size:12px; color:#64748b; margin-top:8px;">Confidence: {conf:.1f}%</div>
        </div>
        ''', unsafe_allow_html=True)

section_divider()

# Clear button
if st.button("🗑️ Clear All Patients"):
    st.session_state.patients_list = []
    st.rerun()

show_disclaimer()
