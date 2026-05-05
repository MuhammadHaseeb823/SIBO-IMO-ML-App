import streamlit as st


def inject_custom_css():
    """Inject clean, highly readable dark-theme CSS."""
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    /* ===== GLOBAL ===== */
    .stApp {
        background-color: #111827;
        color: #ffffff;
        font-family: 'Inter', sans-serif;
    }

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* ===== ALL TEXT WHITE & READABLE ===== */
    .stMarkdown, .stMarkdown p, .stMarkdown li, .stMarkdown span,
    label, .stTextInput label, .stNumberInput label, .stSelectbox label {
        color: #ffffff !important;
        font-size: 16px !important;
    }

    h1 { color: #ffffff !important; font-size: 34px !important; font-weight: 800 !important; }
    h2 { color: #ffffff !important; font-size: 26px !important; font-weight: 700 !important; }
    h3 { color: #ffffff !important; font-size: 20px !important; font-weight: 700 !important; }

    /* ===== SIDEBAR — BRIGHT & READABLE ===== */
    [data-testid="stSidebar"] {
        background-color: #1f2937;
        border-right: 1px solid #374151;
    }

    [data-testid="stSidebar"] * {
        color: #ffffff !important;
    }

    [data-testid="stSidebar"] a {
        color: #93c5fd !important;
        font-size: 16px !important;
        font-weight: 500 !important;
    }

    [data-testid="stSidebar"] a:hover {
        color: #60a5fa !important;
        background-color: rgba(96, 165, 250, 0.1) !important;
    }

    [data-testid="stSidebar"] [data-testid="stSidebarNavItems"] a {
        padding: 8px 12px !important;
        border-radius: 8px !important;
        margin: 2px 0 !important;
    }

    [data-testid="stSidebar"] .stMarkdown p {
        color: #d1d5db !important;
        font-size: 15px !important;
    }

    /* ===== GLASS CARD ===== */
    .glass-card {
        background-color: #1f2937;
        border: 1px solid #374151;
        border-radius: 14px;
        padding: 24px;
        margin-bottom: 16px;
        transition: all 0.3s ease;
        color: #ffffff;
    }

    .glass-card:hover {
        border-color: #60a5fa;
        box-shadow: 0 4px 20px rgba(96, 165, 250, 0.1);
    }

    .glass-card * {
        color: #ffffff !important;
    }

    .glass-card .subtitle {
        color: #9ca3af !important;
    }

    /* ===== GRADIENT TEXT ===== */
    .gradient-text {
        background: linear-gradient(135deg, #60a5fa, #a78bfa);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-weight: 800;
    }

    .gradient-text-lg { font-size: 42px; line-height: 1.1; margin-bottom: 8px; }
    .gradient-text-md { font-size: 28px; line-height: 1.2; }

    /* ===== HERO ===== */
    .hero-section {
        text-align: center;
        padding: 40px 20px 20px;
    }

    .hero-subtitle {
        color: #d1d5db !important;
        font-size: 18px;
        font-weight: 400;
        margin-top: 10px;
    }

    /* ===== METRIC CARD ===== */
    .metric-card {
        background-color: #1f2937;
        border: 1px solid #374151;
        border-radius: 14px;
        padding: 20px;
        text-align: center;
    }

    .metric-value {
        font-size: 34px;
        font-weight: 800;
        color: #60a5fa !important;
    }

    .metric-label {
        color: #d1d5db !important;
        font-size: 14px;
        font-weight: 600;
        margin-top: 6px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    /* ===== DIAGNOSIS BADGES ===== */
    .diagnosis-badge {
        display: inline-block;
        padding: 12px 32px;
        border-radius: 50px;
        font-weight: 700;
        font-size: 20px;
        letter-spacing: 0.5px;
    }

    .badge-sibo { background: #1e3a5f; color: #93c5fd !important; border: 2px solid #3b82f6; }
    .badge-imo { background: #422006; color: #fcd34d !important; border: 2px solid #f59e0b; }
    .badge-both { background: #450a0a; color: #fca5a5 !important; border: 2px solid #ef4444; }
    .badge-none { background: #052e16; color: #86efac !important; border: 2px solid #22c55e; }

    /* ===== BUTTONS ===== */
    .stButton > button {
        background: linear-gradient(135deg, #3b82f6, #8b5cf6);
        color: white !important;
        border: none;
        border-radius: 12px;
        padding: 0.7em 2em;
        font-weight: 700;
        font-size: 16px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(59, 130, 246, 0.3);
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(59, 130, 246, 0.5);
    }

    /* ===== INPUTS ===== */
    .stNumberInput > div > div > input,
    .stTextInput > div > div > input {
        background-color: #1f2937 !important;
        border: 1px solid #4b5563 !important;
        border-radius: 10px !important;
        color: #ffffff !important;
        font-size: 16px !important;
    }

    .stSelectbox > div > div {
        background-color: #1f2937 !important;
        border: 1px solid #4b5563 !important;
        color: #ffffff !important;
    }

    /* ===== CONFIDENCE BAR ===== */
    .confidence-bar-bg {
        background-color: #374151;
        border-radius: 8px;
        height: 32px;
        overflow: hidden;
        margin: 6px 0;
    }

    .confidence-bar-fill {
        height: 100%;
        border-radius: 8px;
        display: flex;
        align-items: center;
        padding-left: 12px;
        font-size: 14px;
        font-weight: 700;
        color: white !important;
        transition: width 0.8s ease;
    }

    /* ===== SECTION DIVIDER ===== */
    .section-divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, #4b5563, transparent);
        margin: 30px 0;
    }

    /* ===== DISCLAIMER ===== */
    .disclaimer-bar {
        background-color: #422006;
        border: 1px solid #92400e;
        border-radius: 10px;
        padding: 14px 20px;
        font-size: 14px;
        color: #fcd34d !important;
        margin: 20px 0;
        line-height: 1.6;
    }

    .disclaimer-bar * {
        color: #fcd34d !important;
    }

    /* ===== TABS ===== */
    .stTabs [data-baseweb="tab-list"] { gap: 8px; }

    .stTabs [data-baseweb="tab"] {
        background-color: #1f2937;
        border-radius: 8px;
        color: #ffffff !important;
        padding: 10px 18px;
        font-size: 15px !important;
    }

    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #1e3a5f, #312e81);
        color: #ffffff !important;
        border-bottom: 2px solid #60a5fa;
    }

    /* ===== DATAFRAME ===== */
    .stDataFrame { border-radius: 12px; overflow: hidden; }

    /* ===== ANIMATIONS ===== */
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .animate-in { animation: fadeInUp 0.6s ease-out forwards; }
    </style>
    """, unsafe_allow_html=True)


def section_divider():
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)


def glass_card(content_html):
    st.markdown(f'<div class="glass-card">{content_html}</div>', unsafe_allow_html=True)


def metric_card(value, label):
    st.markdown(f'''
    <div class="metric-card">
        <div class="metric-value">{value}</div>
        <div class="metric-label">{label}</div>
    </div>
    ''', unsafe_allow_html=True)


def get_diagnosis_badge(diagnosis):
    badge_map = {
        'SIBO': ('badge-sibo', '🔵 SIBO'),
        'IMO': ('badge-imo', '🟠 IMO'),
        'SIBO & IMO': ('badge-both', '🔴 SIBO & IMO'),
        'No Diagnosis': ('badge-none', '🟢 No Diagnosis'),
    }
    css_class, label = badge_map.get(diagnosis, ('badge-none', diagnosis))
    return f'<span class="diagnosis-badge {css_class}">{label}</span>'


def confidence_bar(label, value, color):
    pct = f"{value:.1f}%"
    st.markdown(f'''
    <div style="display:flex; align-items:center; margin:8px 0;">
        <div style="width:150px; font-size:16px; color:#ffffff; font-weight:600;">{label}</div>
        <div class="confidence-bar-bg" style="flex:1;">
            <div class="confidence-bar-fill" style="width:{value}%; background:{color};">{pct}</div>
        </div>
    </div>
    ''', unsafe_allow_html=True)
