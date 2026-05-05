import streamlit as st

# ===== PAGE CONFIG =====
st.set_page_config(
    page_title="SIBO & IMO Clinical AI System",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

from utils.styles import inject_custom_css, section_divider, metric_card
from utils.disclaimer import show_disclaimer

inject_custom_css()

# ===== SIDEBAR =====
with st.sidebar:
    st.markdown("### 🧬 SIBO & IMO AI")
    st.markdown("---")
    st.markdown("**Pages**")
    st.markdown("""
    - 🔬 Diagnosis
    - 📊 AI Insights
    - 👥 Patient Comparison
    - 📄 Report Export
    - 📖 How It Works
    """)
    st.markdown("---")
    show_disclaimer()

# ===== HERO =====
st.markdown('''
<div class="hero-section animate-in">
    <div style="font-size:48px; margin-bottom:8px;">🧬</div>
    <div class="gradient-text gradient-text-lg">SIBO & IMO Clinical AI System</div>
    <div class="hero-subtitle">
        Machine Learning Powered Breath Test Diagnostic Tool
    </div>
</div>
''', unsafe_allow_html=True)

section_divider()

# ===== STATS ROW =====
sc1, sc2, sc3, sc4 = st.columns(4)
with sc1:
    metric_card("96.12%", "Model Accuracy")
with sc2:
    metric_card("511", "Patients Trained On")
with sc3:
    metric_card("4", "Diagnosis Classes")
with sc4:
    metric_card("8", "Input Features")

section_divider()

# ===== FEATURE CARDS =====
st.markdown('<div class="gradient-text gradient-text-md">🚀 System Features</div>', unsafe_allow_html=True)
st.markdown("")

fc1, fc2, fc3 = st.columns(3)

with fc1:
    st.markdown('''
    <div class="glass-card" style="min-height:200px;">
        <div style="font-size:28px; margin-bottom:8px;">🔬</div>
        <div style="font-size:18px; font-weight:700; color:#f1f5f9; margin-bottom:8px;">AI Diagnosis</div>
        <div style="font-size:14px; color:#94a3b8; line-height:1.6;">
            Enter patient breath test values and receive an instant AI-powered diagnosis with
            confidence scores for SIBO, IMO, combined, or no diagnosis.
        </div>
    </div>
    ''', unsafe_allow_html=True)

with fc2:
    st.markdown('''
    <div class="glass-card" style="min-height:200px;">
        <div style="font-size:28px; margin-bottom:8px;">📊</div>
        <div style="font-size:18px; font-weight:700; color:#f1f5f9; margin-bottom:8px;">AI Insights</div>
        <div style="font-size:14px; color:#94a3b8; line-height:1.6;">
            Explore feature importance charts, patient risk profiles, clinical interpretations,
            and reference ranges to understand the prediction.
        </div>
    </div>
    ''', unsafe_allow_html=True)

with fc3:
    st.markdown('''
    <div class="glass-card" style="min-height:200px;">
        <div style="font-size:28px; margin-bottom:8px;">👥</div>
        <div style="font-size:18px; font-weight:700; color:#f1f5f9; margin-bottom:8px;">Patient Comparison</div>
        <div style="font-size:14px; color:#94a3b8; line-height:1.6;">
            Compare multiple patients side-by-side with interactive charts, diagnosis matrices,
            and detailed gas level breakdowns.
        </div>
    </div>
    ''', unsafe_allow_html=True)

fc4, fc5, fc6 = st.columns(3)

with fc4:
    st.markdown('''
    <div class="glass-card" style="min-height:200px;">
        <div style="font-size:28px; margin-bottom:8px;">📄</div>
        <div style="font-size:18px; font-weight:700; color:#f1f5f9; margin-bottom:8px;">PDF Reports</div>
        <div style="font-size:14px; color:#94a3b8; line-height:1.6;">
            Generate and download professional PDF diagnostic reports with patient demographics,
            test values, predictions, and confidence breakdowns.
        </div>
    </div>
    ''', unsafe_allow_html=True)

with fc5:
    st.markdown('''
    <div class="glass-card" style="min-height:200px;">
        <div style="font-size:28px; margin-bottom:8px;">📖</div>
        <div style="font-size:18px; font-weight:700; color:#f1f5f9; margin-bottom:8px;">Educational Content</div>
        <div style="font-size:14px; color:#94a3b8; line-height:1.6;">
            Learn about SIBO, IMO, breath testing methodology, and how the Random Forest
            machine learning model makes predictions.
        </div>
    </div>
    ''', unsafe_allow_html=True)

with fc6:
    st.markdown('''
    <div class="glass-card" style="min-height:200px;">
        <div style="font-size:28px; margin-bottom:8px;">⚡</div>
        <div style="font-size:18px; font-weight:700; color:#f1f5f9; margin-bottom:8px;">High Performance</div>
        <div style="font-size:14px; color:#94a3b8; line-height:1.6;">
            Cached model loading for instant predictions, interactive Plotly charts,
            and a responsive design optimised for clinical workflows.
        </div>
    </div>
    ''', unsafe_allow_html=True)

section_divider()

# ===== QUICK START =====
st.markdown('<div class="gradient-text gradient-text-md">⚡ Quick Start</div>', unsafe_allow_html=True)
st.markdown("")

st.markdown('''
<div class="glass-card">
    <div style="font-size:15px; color:#94a3b8; line-height:2;">
        <strong style="color:#38bdf8;">Step 1:</strong> Navigate to <strong>🔬 Diagnosis</strong> from the sidebar<br>
        <strong style="color:#38bdf8;">Step 2:</strong> Enter patient demographics and breath test values<br>
        <strong style="color:#38bdf8;">Step 3:</strong> Click <strong>Predict</strong> to get an AI-powered diagnosis<br>
        <strong style="color:#38bdf8;">Step 4:</strong> Explore <strong>📊 AI Insights</strong> for detailed analysis<br>
        <strong style="color:#38bdf8;">Step 5:</strong> Download a <strong>📄 PDF Report</strong> for documentation
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
    <div class="metric-card" style="border-left: 3px solid #38bdf8;">
        <div style="font-size:24px; margin-bottom:4px;">🔵</div>
        <div style="font-weight:700; color:#38bdf8;">SIBO</div>
        <div style="font-size:12px; color:#64748b; margin-top:4px;">Hydrogen-dominant bacterial overgrowth</div>
    </div>
    ''', unsafe_allow_html=True)

with dc2:
    st.markdown('''
    <div class="metric-card" style="border-left: 3px solid #f59e0b;">
        <div style="font-size:24px; margin-bottom:4px;">🟠</div>
        <div style="font-weight:700; color:#f59e0b;">IMO</div>
        <div style="font-size:12px; color:#64748b; margin-top:4px;">Methane-producing methanogen overgrowth</div>
    </div>
    ''', unsafe_allow_html=True)

with dc3:
    st.markdown('''
    <div class="metric-card" style="border-left: 3px solid #ef4444;">
        <div style="font-size:24px; margin-bottom:4px;">🔴</div>
        <div style="font-weight:700; color:#ef4444;">SIBO & IMO</div>
        <div style="font-size:12px; color:#64748b; margin-top:4px;">Combined bacterial and archaeal overgrowth</div>
    </div>
    ''', unsafe_allow_html=True)

with dc4:
    st.markdown('''
    <div class="metric-card" style="border-left: 3px solid #22c55e;">
        <div style="font-size:24px; margin-bottom:4px;">🟢</div>
        <div style="font-weight:700; color:#22c55e;">No Diagnosis</div>
        <div style="font-size:12px; color:#64748b; margin-top:4px;">Gas levels within normal parameters</div>
    </div>
    ''', unsafe_allow_html=True)

section_divider()
show_disclaimer()

st.markdown('''
<div style="text-align:center; color:#475569; font-size:12px; padding:20px 0;">
    SIBO & IMO Clinical AI System v2.0 — Built with Streamlit & scikit-learn
</div>
''', unsafe_allow_html=True)
