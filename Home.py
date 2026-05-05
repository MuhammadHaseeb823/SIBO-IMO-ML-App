import streamlit as st

# ===== PAGE CONFIG =====
st.set_page_config(
    page_title="Home | SIBO & IMO Clinical AI",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

from utils.styles import inject_custom_css, section_divider
from utils.disclaimer import show_disclaimer

inject_custom_css()

# ===== SIDEBAR =====
with st.sidebar:
    st.markdown("### 🧬 SIBO & IMO AI")
    st.markdown("---")
    show_disclaimer()

# ===== HERO =====
st.markdown('''
<div class="hero-section animate-in">
    <div style="font-size:52px; margin-bottom:12px;">🧬</div>
    <div class="gradient-text gradient-text-lg">SIBO & IMO Clinical AI System</div>
    <div class="hero-subtitle">Machine Learning Powered Breath Test Diagnostic Tool</div>
</div>
''', unsafe_allow_html=True)

section_divider()

# ===== FEATURE CARDS =====
st.markdown('<div class="gradient-text gradient-text-md">🚀 System Features</div>', unsafe_allow_html=True)
st.markdown("")

fc1, fc2 = st.columns(2)

with fc1:
    st.markdown('''
    <div class="glass-card">
        <div style="font-size:28px; margin-bottom:10px;">🔬</div>
        <div style="font-size:20px; font-weight:700; margin-bottom:10px;">AI Diagnosis</div>
        <div style="font-size:16px; color:#d1d5db; line-height:1.7;">
            Enter patient breath test values and receive an instant AI-powered diagnosis with
            confidence scores for SIBO, IMO, combined, or no diagnosis.
        </div>
    </div>
    ''', unsafe_allow_html=True)

with fc2:
    st.markdown('''
    <div class="glass-card">
        <div style="font-size:28px; margin-bottom:10px;">📊</div>
        <div style="font-size:20px; font-weight:700; margin-bottom:10px;">AI Insights</div>
        <div style="font-size:16px; color:#d1d5db; line-height:1.7;">
            Explore feature importance charts, patient risk profiles, clinical interpretations,
            and reference ranges to understand the prediction.
        </div>
    </div>
    ''', unsafe_allow_html=True)

fc3, fc4 = st.columns(2)

with fc3:
    st.markdown('''
    <div class="glass-card">
        <div style="font-size:28px; margin-bottom:10px;">📄</div>
        <div style="font-size:20px; font-weight:700; margin-bottom:10px;">PDF Reports</div>
        <div style="font-size:16px; color:#d1d5db; line-height:1.7;">
            Generate and download professional PDF diagnostic reports with test values,
            predictions, confidence scores, and clinical interpretation.
        </div>
    </div>
    ''', unsafe_allow_html=True)

with fc4:
    st.markdown('''
    <div class="glass-card">
        <div style="font-size:28px; margin-bottom:10px;">📖</div>
        <div style="font-size:20px; font-weight:700; margin-bottom:10px;">How It Works</div>
        <div style="font-size:16px; color:#d1d5db; line-height:1.7;">
            Learn about SIBO, IMO, breath testing methodology, and how the Random Forest
            machine learning model makes its predictions.
        </div>
    </div>
    ''', unsafe_allow_html=True)

section_divider()

# ===== QUICK START =====
st.markdown('<div class="gradient-text gradient-text-md">⚡ Quick Start</div>', unsafe_allow_html=True)
st.markdown("")

st.markdown('''
<div class="glass-card">
    <div style="font-size:16px; line-height:2.2;">
        <strong style="color:#60a5fa;">Step 1:</strong> Navigate to <strong>🔬 Diagnosis</strong> from the sidebar<br>
        <strong style="color:#60a5fa;">Step 2:</strong> Enter patient demographics and breath test values<br>
        <strong style="color:#60a5fa;">Step 3:</strong> Click <strong>Predict</strong> to get an AI-powered diagnosis<br>
        <strong style="color:#60a5fa;">Step 4:</strong> Explore <strong>📊 AI Insights</strong> for detailed analysis<br>
        <strong style="color:#60a5fa;">Step 5:</strong> Download a <strong>📄 PDF Report</strong> for documentation
    </div>
</div>
''', unsafe_allow_html=True)

section_divider()

# ===== DIAGNOSIS CLASSES =====
st.markdown('<div class="gradient-text gradient-text-md">🎯 Diagnostic Classes</div>', unsafe_allow_html=True)
st.markdown("")

dc1, dc2, dc3, dc4 = st.columns(4)

with dc1:
    st.markdown('''
    <div class="metric-card" style="border-left: 3px solid #3b82f6;">
        <div style="font-size:24px;">🔵</div>
        <div style="font-weight:700; color:#93c5fd !important; font-size:18px; margin-top:6px;">SIBO</div>
        <div style="font-size:13px; color:#9ca3af !important; margin-top:4px;">Hydrogen-dominant bacterial overgrowth</div>
    </div>
    ''', unsafe_allow_html=True)

with dc2:
    st.markdown('''
    <div class="metric-card" style="border-left: 3px solid #f59e0b;">
        <div style="font-size:24px;">🟠</div>
        <div style="font-weight:700; color:#fcd34d !important; font-size:18px; margin-top:6px;">IMO</div>
        <div style="font-size:13px; color:#9ca3af !important; margin-top:4px;">Methane-producing methanogen overgrowth</div>
    </div>
    ''', unsafe_allow_html=True)

with dc3:
    st.markdown('''
    <div class="metric-card" style="border-left: 3px solid #ef4444;">
        <div style="font-size:24px;">🔴</div>
        <div style="font-weight:700; color:#fca5a5 !important; font-size:18px; margin-top:6px;">SIBO & IMO</div>
        <div style="font-size:13px; color:#9ca3af !important; margin-top:4px;">Combined bacterial & archaeal overgrowth</div>
    </div>
    ''', unsafe_allow_html=True)

with dc4:
    st.markdown('''
    <div class="metric-card" style="border-left: 3px solid #22c55e;">
        <div style="font-size:24px;">🟢</div>
        <div style="font-weight:700; color:#86efac !important; font-size:18px; margin-top:6px;">No Diagnosis</div>
        <div style="font-size:13px; color:#9ca3af !important; margin-top:4px;">Gas levels within normal parameters</div>
    </div>
    ''', unsafe_allow_html=True)

section_divider()
show_disclaimer()
