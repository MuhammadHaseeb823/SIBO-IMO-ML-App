import streamlit as st


def inject_custom_css():
    """Inject premium dark-theme CSS across all pages."""
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

    /* ===== GLOBAL ===== */
    .stApp {
        background: linear-gradient(135deg, #0b1220 0%, #0f172a 40%, #020617 100%);
        color: #e2e8f0;
        font-family: 'Inter', sans-serif;
    }

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* ===== SIDEBAR ===== */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f172a 0%, #1e1b4b 100%);
        border-right: 1px solid rgba(99, 102, 241, 0.15);
    }

    [data-testid="stSidebar"] .stMarkdown h1,
    [data-testid="stSidebar"] .stMarkdown h2,
    [data-testid="stSidebar"] .stMarkdown h3 {
        color: #c7d2fe;
    }

    [data-testid="stSidebar"] .stMarkdown p,
    [data-testid="stSidebar"] .stMarkdown li {
        color: #94a3b8;
    }

    /* ===== HEADINGS ===== */
    h1, h2, h3 { color: #f1f5f9; }

    /* ===== GLASS CARD ===== */
    .glass-card {
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 24px;
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        margin-bottom: 16px;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .glass-card:hover {
        border-color: rgba(99, 102, 241, 0.3);
        box-shadow: 0 8px 32px rgba(99, 102, 241, 0.08);
        transform: translateY(-2px);
    }

    /* ===== GRADIENT TEXT ===== */
    .gradient-text {
        background: linear-gradient(135deg, #38bdf8 0%, #a78bfa 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-weight: 800;
    }

    .gradient-text-lg {
        font-size: 42px;
        line-height: 1.1;
        margin-bottom: 8px;
    }

    .gradient-text-md {
        font-size: 28px;
        line-height: 1.2;
    }

    /* ===== HERO ===== */
    .hero-section {
        text-align: center;
        padding: 40px 20px 30px;
    }

    .hero-subtitle {
        color: #94a3b8;
        font-size: 16px;
        font-weight: 400;
        margin-top: 8px;
    }

    /* ===== METRIC CARD ===== */
    .metric-card {
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 14px;
        padding: 20px;
        text-align: center;
        transition: all 0.3s ease;
    }

    .metric-card:hover {
        border-color: rgba(56, 189, 248, 0.3);
        box-shadow: 0 4px 20px rgba(56, 189, 248, 0.08);
    }

    .metric-value {
        font-size: 32px;
        font-weight: 800;
        background: linear-gradient(135deg, #38bdf8, #a78bfa);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .metric-label {
        color: #94a3b8;
        font-size: 13px;
        font-weight: 500;
        margin-top: 4px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    /* ===== DIAGNOSIS BADGES ===== */
    .diagnosis-badge {
        display: inline-block;
        padding: 10px 28px;
        border-radius: 50px;
        font-weight: 700;
        font-size: 18px;
        text-align: center;
        letter-spacing: 0.5px;
    }

    .badge-sibo { background: rgba(56, 189, 248, 0.15); color: #38bdf8; border: 1px solid rgba(56, 189, 248, 0.3); }
    .badge-imo { background: rgba(245, 158, 11, 0.15); color: #f59e0b; border: 1px solid rgba(245, 158, 11, 0.3); }
    .badge-both { background: rgba(239, 68, 68, 0.15); color: #ef4444; border: 1px solid rgba(239, 68, 68, 0.3); }
    .badge-none { background: rgba(34, 197, 94, 0.15); color: #22c55e; border: 1px solid rgba(34, 197, 94, 0.3); }

    /* ===== BUTTONS ===== */
    .stButton > button {
        background: linear-gradient(135deg, #38bdf8 0%, #a78bfa 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.6em 2em;
        font-weight: 600;
        font-size: 15px;
        letter-spacing: 0.3px;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 4px 15px rgba(56, 189, 248, 0.2);
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(56, 189, 248, 0.35);
    }

    .stButton > button:active {
        transform: translateY(0);
    }

    /* ===== INPUTS ===== */
    .stNumberInput > div > div > input,
    .stTextInput > div > div > input,
    .stSelectbox > div > div {
        background: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 10px !important;
        color: #e2e8f0 !important;
    }

    .stNumberInput > div > div > input:focus,
    .stTextInput > div > div > input:focus {
        border-color: rgba(56, 189, 248, 0.5) !important;
        box-shadow: 0 0 0 2px rgba(56, 189, 248, 0.1) !important;
    }

    /* ===== EXPANDER ===== */
    .streamlit-expanderHeader {
        background: rgba(255, 255, 255, 0.04);
        border-radius: 10px;
        color: #c7d2fe;
    }

    /* ===== CONFIDENCE BAR ===== */
    .confidence-bar-bg {
        background: rgba(255, 255, 255, 0.06);
        border-radius: 8px;
        height: 28px;
        overflow: hidden;
        margin: 4px 0;
    }

    .confidence-bar-fill {
        height: 100%;
        border-radius: 8px;
        display: flex;
        align-items: center;
        padding-left: 10px;
        font-size: 12px;
        font-weight: 600;
        color: white;
        transition: width 0.8s cubic-bezier(0.4, 0, 0.2, 1);
    }

    /* ===== SECTION DIVIDER ===== */
    .section-divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(99,102,241,0.3), transparent);
        margin: 30px 0;
    }

    /* ===== DISCLAIMER ===== */
    .disclaimer-bar {
        background: rgba(245, 158, 11, 0.08);
        border: 1px solid rgba(245, 158, 11, 0.25);
        border-radius: 10px;
        padding: 12px 18px;
        font-size: 13px;
        color: #fbbf24;
        margin: 20px 0;
        line-height: 1.5;
    }

    /* ===== TABLE ===== */
    .stDataFrame {
        border-radius: 12px;
        overflow: hidden;
    }

    /* ===== TABS ===== */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }

    .stTabs [data-baseweb="tab"] {
        background: rgba(255, 255, 255, 0.04);
        border-radius: 8px;
        color: #94a3b8;
        padding: 8px 16px;
    }

    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, rgba(56,189,248,0.15), rgba(167,139,250,0.15));
        color: #f1f5f9;
    }

    /* ===== ANIMATION KEYFRAMES ===== */
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .animate-in {
        animation: fadeInUp 0.6s ease-out forwards;
    }

    /* ===== PULSE GLOW ===== */
    @keyframes pulseGlow {
        0%, 100% { box-shadow: 0 0 5px rgba(56, 189, 248, 0.2); }
        50% { box-shadow: 0 0 20px rgba(56, 189, 248, 0.4); }
    }

    .pulse-glow {
        animation: pulseGlow 2s ease-in-out infinite;
    }
    </style>
    """, unsafe_allow_html=True)


def section_divider():
    """Render a gradient divider line."""
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)


def glass_card(content_html):
    """Wrap content in a glass card."""
    st.markdown(f'<div class="glass-card">{content_html}</div>', unsafe_allow_html=True)


def metric_card(value, label):
    """Render a styled metric card."""
    st.markdown(f'''
    <div class="metric-card">
        <div class="metric-value">{value}</div>
        <div class="metric-label">{label}</div>
    </div>
    ''', unsafe_allow_html=True)


def get_diagnosis_badge(diagnosis):
    """Return the badge HTML for a diagnosis."""
    badge_map = {
        'SIBO': ('badge-sibo', '🔵 SIBO'),
        'IMO': ('badge-imo', '🟠 IMO'),
        'SIBO & IMO': ('badge-both', '🔴 SIBO & IMO'),
        'No Diagnosis': ('badge-none', '🟢 No Diagnosis'),
    }
    css_class, label = badge_map.get(diagnosis, ('badge-none', diagnosis))
    return f'<span class="diagnosis-badge {css_class}">{label}</span>'


def confidence_bar(label, value, color):
    """Render a confidence percentage bar."""
    pct = f"{value:.1f}%"
    st.markdown(f'''
    <div style="display:flex; align-items:center; margin:6px 0;">
        <div style="width:140px; font-size:13px; color:#94a3b8; font-weight:500;">{label}</div>
        <div class="confidence-bar-bg" style="flex:1;">
            <div class="confidence-bar-fill" style="width:{value}%; background:{color};">{pct}</div>
        </div>
    </div>
    ''', unsafe_allow_html=True)
