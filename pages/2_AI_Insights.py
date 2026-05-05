import streamlit as st
import sys
import os
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.styles import inject_custom_css, section_divider, glass_card, get_diagnosis_badge
from utils.disclaimer import show_disclaimer
from utils.model_utils import (
    get_feature_importance, get_clinical_interpretation,
    REFERENCE_RANGES, DIAGNOSIS_COLORS,
)

st.set_page_config(page_title="AI Insights | SIBO & IMO AI", layout="wide", initial_sidebar_state="expanded")
inject_custom_css()

with st.sidebar:
    st.markdown("### 🧬 SIBO & IMO AI")
    st.markdown("---")
    show_disclaimer()

# ===== HERO =====
st.markdown('''
<div class="hero-section animate-in">
    <div class="gradient-text gradient-text-lg">📊 AI Insights & Analysis</div>
    <div class="hero-subtitle">Deep-dive into model predictions, feature importance, and clinical interpretation</div>
</div>
''', unsafe_allow_html=True)

section_divider()

# Check if a prediction exists
if 'current_patient' not in st.session_state or not st.session_state.current_patient:
    st.warning("⚠️ No prediction data found. Please go to the **Diagnosis** page and run a prediction first.")
    show_disclaimer()
    st.stop()

patient = st.session_state.current_patient
diagnosis = patient['diagnosis']
probabilities = patient['probabilities']
inputs = patient['inputs']

# ===== DIAGNOSIS RECAP =====
badge_html = get_diagnosis_badge(diagnosis)
st.markdown(f'''
<div class="glass-card" style="text-align:center;">
    <span style="color:#94a3b8; font-size:13px;">Current Prediction</span>
    <div style="margin:8px 0;">{badge_html}</div>
    <span style="color:#64748b; font-size:12px;">
        Age: {inputs.get("Age", "N/A")} | Gender: {patient.get("gender", "N/A")}
    </span>
</div>
''', unsafe_allow_html=True)

section_divider()

# ===== TABS =====
tab1, tab2, tab3, tab4 = st.tabs([
    "🏗️ Feature Importance",
    "🎯 Patient Risk Profile",
    "🩺 Clinical Interpretation",
    "📏 Reference Ranges"
])

# ----- TAB 1: Feature Importance -----
with tab1:
    st.markdown("### Which features does the model rely on most?")
    st.markdown("The Random Forest model assigns importance scores to each input feature. "
                "Higher scores mean the feature has more influence on predictions.")
    st.markdown("")

    fi = get_feature_importance()
    fi_sorted = dict(sorted(fi.items(), key=lambda x: x[1]))

    fig = go.Figure(go.Bar(
        x=list(fi_sorted.values()),
        y=list(fi_sorted.keys()),
        orientation='h',
        marker=dict(
            color=list(fi_sorted.values()),
            colorscale=[[0, '#38bdf8'], [0.5, '#818cf8'], [1, '#a78bfa']],
        ),
        hovertemplate='<b>%{y}</b><br>Importance: %{x:.4f}<extra></extra>',
    ))

    fig.update_layout(
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        height=400,
        margin=dict(l=10, r=10, t=10, b=10),
        xaxis_title='Importance Score',
        yaxis_title='',
        font=dict(family='Inter', color='#94a3b8'),
    )
    st.plotly_chart(fig, use_container_width=True)

    st.info("💡 **Tip:** Features with higher importance have more impact on whether "
            "the model predicts SIBO, IMO, both, or no diagnosis.")

# ----- TAB 2: Radar Chart -----
with tab2:
    st.markdown("### Patient value profile compared to typical thresholds")
    st.markdown("")

    # Normalise patient values to a 0–100 scale for radar display
    radar_features = [k for k in inputs if k != 'Age']
    max_vals = {
        'Baseline H₂ (ppm)': 30, 'Baseline CH₄ (ppm)': 20,
        'Peak H₂ (ppm)': 150, 'Peak CH₄ (ppm)': 80,
        'Combined Peak (ppm)': 200, 'Time of Peak (minutes)': 180,
        'Increase from Baseline (ppm)': 150,
    }
    radar_vals = [min((inputs[f] / max_vals.get(f, 100)) * 100, 100) for f in radar_features]
    radar_labels = [f.replace(' (ppm)', '').replace(' (minutes)', '') for f in radar_features]

    fig_radar = go.Figure()
    fig_radar.add_trace(go.Scatterpolar(
        r=radar_vals + [radar_vals[0]],
        theta=radar_labels + [radar_labels[0]],
        fill='toself',
        fillcolor='rgba(56, 189, 248, 0.15)',
        line=dict(color='#38bdf8', width=2),
        name='Patient Values',
    ))

    fig_radar.update_layout(
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        height=450,
        polar=dict(
            bgcolor='rgba(0,0,0,0)',
            radialaxis=dict(visible=True, range=[0, 100], color='#475569'),
            angularaxis=dict(color='#94a3b8'),
        ),
        font=dict(family='Inter', color='#94a3b8'),
        showlegend=False,
        margin=dict(l=60, r=60, t=30, b=30),
    )
    st.plotly_chart(fig_radar, use_container_width=True)

    # Show raw values
    st.markdown("**Raw Values:**")
    val_cols = st.columns(len(radar_features))
    for i, f in enumerate(radar_features):
        with val_cols[i]:
            st.metric(label=radar_labels[i], value=f"{inputs[f]:.1f}")

# ----- TAB 3: Clinical Interpretation -----
with tab3:
    st.markdown("### AI-Generated Clinical Interpretation")
    st.markdown("This interpretation is based on established clinical thresholds for breath test analysis.")
    st.markdown("")

    interpretation = get_clinical_interpretation(diagnosis, inputs)
    st.markdown(f'<div class="glass-card">{interpretation.replace(chr(10), "<br>")}</div>',
                unsafe_allow_html=True)

    st.markdown("")
    st.markdown("### 📚 Further Reading")
    st.markdown("""
    - **North American Consensus (2017):** Hydrogen and methane-based breath testing in gastrointestinal disorders
    - **ACG Clinical Guideline (2020):** Small Intestinal Bacterial Overgrowth
    - **Pimentel et al. (2020):** ACG Clinical Guideline on SIBO — *American Journal of Gastroenterology*
    - **Rezaie et al. (2017):** Hydrogen and Methane-Based Breath Testing — *American Journal of Gastroenterology*

    > These references are for educational context. Always verify with the latest published guidelines.
    """)

# ----- TAB 4: Reference Ranges -----
with tab4:
    st.markdown("### Standard Reference Ranges for Breath Test Interpretation")
    st.markdown("")

    ref_data = []
    for param, info in REFERENCE_RANGES.items():
        display_param = param.replace('\u2082', '2').replace('\u2084', '4')
        patient_val = inputs.get(param, 'N/A')
        ref_data.append({
            'Parameter': display_param,
            'Normal Range': info['normal'],
            'Elevated': info['elevated'],
            'Patient Value': f"{patient_val:.1f}" if isinstance(patient_val, (int, float)) else patient_val,
            'Clinical Note': info['note'],
        })

    df_ref = pd.DataFrame(ref_data)
    st.dataframe(df_ref, use_container_width=True, hide_index=True)

    st.markdown("")
    st.info("📖 These reference ranges are based on published clinical guidelines "
            "and are provided for educational comparison only.")

section_divider()
show_disclaimer()
