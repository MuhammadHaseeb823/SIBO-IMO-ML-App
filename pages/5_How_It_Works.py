import streamlit as st
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.styles import inject_custom_css, section_divider, glass_card, metric_card
from utils.disclaimer import show_disclaimer

st.set_page_config(page_title="How It Works | SIBO & IMO AI", layout="wide", initial_sidebar_state="expanded")
inject_custom_css()

with st.sidebar:
    st.markdown("### 🧬 SIBO & IMO AI")
    st.markdown("---")
    show_disclaimer()

# ===== HERO =====
st.markdown('''
<div class="hero-section animate-in">
    <div class="gradient-text gradient-text-lg">📖 How It Works</div>
    <div class="hero-subtitle">Understanding the science behind SIBO, IMO, and our AI diagnostic system</div>
</div>
''', unsafe_allow_html=True)

section_divider()

# ===== SECTION 1: What is SIBO & IMO? =====
st.markdown('<div class="gradient-text gradient-text-md">🦠 What is SIBO & IMO?</div>', unsafe_allow_html=True)
st.markdown("")

col1, col2 = st.columns(2)
with col1:
    st.markdown('''
    <div class="glass-card">
        <div style="font-size:20px; font-weight:700; color:#38bdf8; margin-bottom:10px;">🔵 SIBO</div>
        <div style="font-size:15px; color:#94a3b8; line-height:1.7;">
            <strong>Small Intestinal Bacterial Overgrowth</strong> occurs when excessive bacteria
            colonise the small intestine, leading to symptoms like bloating, diarrhoea, abdominal pain,
            and malabsorption. These bacteria ferment carbohydrates and produce <strong>hydrogen gas (H₂)</strong>,
            which is detected through breath testing.
        </div>
    </div>
    ''', unsafe_allow_html=True)

with col2:
    st.markdown('''
    <div class="glass-card">
        <div style="font-size:20px; font-weight:700; color:#f59e0b; margin-bottom:10px;">🟠 IMO</div>
        <div style="font-size:15px; color:#94a3b8; line-height:1.7;">
            <strong>Intestinal Methanogen Overgrowth</strong> is characterised by an excess of
            methane-producing archaea (methanogens) in the gut. Unlike SIBO bacteria, methanogens
            produce <strong>methane gas (CH₄)</strong>. IMO is commonly associated with constipation-predominant
            symptoms and can occur throughout the entire GI tract.
        </div>
    </div>
    ''', unsafe_allow_html=True)

st.markdown('''
<div class="glass-card">
    <div style="font-size:20px; font-weight:700; color:#ef4444; margin-bottom:10px;">🔴 SIBO & IMO (Combined)</div>
    <div style="font-size:15px; color:#94a3b8; line-height:1.7;">
        Some patients present with <strong>both conditions simultaneously</strong>, showing elevated levels
        of both hydrogen and methane gases. This combined pattern may result in mixed symptom presentations
        and often requires a more comprehensive treatment approach targeting both bacterial and archaeal organisms.
    </div>
</div>
''', unsafe_allow_html=True)

section_divider()

# ===== SECTION 2: The Breath Test =====
st.markdown('<div class="gradient-text gradient-text-md">🫁 How the Breath Test Works</div>', unsafe_allow_html=True)
st.markdown("")

st.markdown('''
<div class="glass-card">
    <div style="font-size:15px; color:#94a3b8; line-height:1.8;">
        The <strong>lactulose or glucose breath test</strong> is the primary non-invasive method for diagnosing SIBO and IMO:
        <br><br>
        <strong>1. Preparation:</strong> The patient fasts for 12 hours and avoids certain foods the day before.
        <br><br>
        <strong>2. Baseline Measurement:</strong> A baseline breath sample is collected to measure resting H₂ and CH₄ levels.
        <br><br>
        <strong>3. Substrate Ingestion:</strong> The patient drinks a lactulose or glucose solution.
        <br><br>
        <strong>4. Serial Sampling:</strong> Breath samples are collected every 15–20 minutes for 2–3 hours.
        <br><br>
        <strong>5. Analysis:</strong> H₂ and CH₄ concentrations are measured at each time point to identify abnormal patterns.
    </div>
</div>
''', unsafe_allow_html=True)

st.markdown("")
st.markdown("**Key Diagnostic Thresholds:**")

tc1, tc2, tc3 = st.columns(3)
with tc1:
    st.markdown('''
    <div class="metric-card">
        <div class="metric-value">≥ 20 ppm</div>
        <div class="metric-label">H₂ rise from baseline → SIBO</div>
    </div>
    ''', unsafe_allow_html=True)
with tc2:
    st.markdown('''
    <div class="metric-card">
        <div class="metric-value">≥ 10 ppm</div>
        <div class="metric-label">CH₄ at any point → IMO</div>
    </div>
    ''', unsafe_allow_html=True)
with tc3:
    st.markdown('''
    <div class="metric-card">
        <div class="metric-value">< 90 min</div>
        <div class="metric-label">Early peak → Proximal SIBO</div>
    </div>
    ''', unsafe_allow_html=True)

section_divider()

# ===== SECTION 3: The ML Model =====
st.markdown('<div class="gradient-text gradient-text-md">🤖 The Machine Learning Model</div>', unsafe_allow_html=True)
st.markdown("")

mc1, mc2, mc3, mc4 = st.columns(4)
with mc1:
    metric_card("96.12%", "Model Accuracy")
with mc2:
    metric_card("511", "Training Samples")
with mc3:
    metric_card("100", "Decision Trees")
with mc4:
    metric_card("4", "Diagnosis Classes")

st.markdown("")

st.markdown('''
<div class="glass-card">
    <div style="font-size:18px; font-weight:700; color:#f1f5f9; margin-bottom:12px;">Random Forest Classifier</div>
    <div style="font-size:15px; color:#94a3b8; line-height:1.8;">
        Our system uses a <strong>Random Forest Classifier</strong> — an ensemble machine learning algorithm
        that builds 100 individual decision trees and combines their predictions through majority voting.
        <br><br>
        <strong>How it works:</strong>
        <br>• Each tree is trained on a random subset of the training data (bootstrapping)
        <br>• At each split, a random subset of features is considered
        <br>• The final prediction is the class that receives the most votes across all trees
        <br>• This approach reduces overfitting and provides robust, reliable predictions
        <br><br>
        <strong>Training process:</strong>
        <br>• Dataset: 511 patient records with confirmed diagnoses
        <br>• 80/20 train-test split with random_state=42 for reproducibility
        <br>• Features standardised using StandardScaler (zero mean, unit variance)
        <br>• Labels encoded using LabelEncoder for the 4 diagnostic classes
        <br><br>
        <strong>Performance metrics:</strong>
        <br>• Overall accuracy: 96.12%
        <br>• IMO — Precision: 93%, Recall: 88%
        <br>• No Diagnosis — Precision: 98%, Recall: 100%
        <br>• SIBO — Precision: 100%, Recall: 88%
        <br>• SIBO & IMO — Precision: 95%, Recall: 97%
    </div>
</div>
''', unsafe_allow_html=True)

section_divider()

# ===== SECTION 4: Features Explained =====
st.markdown('<div class="gradient-text gradient-text-md">📐 Input Features Explained</div>', unsafe_allow_html=True)
st.markdown("")

features_info = [
    ("Age", "Patient's age in years. Age may influence gut microbiome composition and test interpretation."),
    ("Baseline H₂ (ppm)", "Fasting hydrogen level before substrate ingestion. Elevated baselines (>10 ppm) may indicate recent carbohydrate fermentation."),
    ("Baseline CH₄ (ppm)", "Fasting methane level. Elevated baselines suggest existing methanogen activity."),
    ("Peak H₂ (ppm)", "Highest hydrogen reading during the test. A rise ≥20 ppm above baseline is considered positive for SIBO."),
    ("Peak CH₄ (ppm)", "Highest methane reading. Levels ≥10 ppm at any point are consistent with IMO."),
    ("Combined Peak (ppm)", "Sum of peak H₂ and CH₄, reflecting total gas production from microbial fermentation."),
    ("Time of Peak (minutes)", "When the gas peak occurs. Early peaks (<90 min) may indicate proximal small bowel involvement."),
    ("Increase from Baseline (ppm)", "The maximum rise in gas levels from the baseline measurement."),
]

for fname, fdesc in features_info:
    st.markdown(f'''
    <div class="glass-card" style="padding:16px;">
        <span style="font-weight:700; color:#38bdf8;">{fname}</span>
        <span style="color:#94a3b8; margin-left:12px;">{fdesc}</span>
    </div>
    ''', unsafe_allow_html=True)

section_divider()

# ===== SECTION 5: Limitations =====
st.markdown('<div class="gradient-text gradient-text-md">⚖️ Model Limitations</div>', unsafe_allow_html=True)
st.markdown("")

st.markdown('''
<div class="glass-card">
    <div style="font-size:15px; color:#94a3b8; line-height:1.8;">
        <strong>1. Dataset Size:</strong> The model was trained on 511 patient records. While this provides
        reasonable accuracy, larger datasets could improve generalisability.
        <br><br>
        <strong>2. Gender Not Included:</strong> Gender was not used as a model feature during training.
        It is collected for demographic reporting purposes only.
        <br><br>
        <strong>3. Population Bias:</strong> Model performance depends on the training population demographics.
        Results may vary for populations significantly different from the training data.
        <br><br>
        <strong>4. Clinical Context:</strong> The model considers only breath test values. Real clinical diagnosis
        involves patient history, symptoms, physical examination, and other diagnostic tests.
        <br><br>
        <strong>5. Not a Diagnostic Tool:</strong> This is an educational demonstration of machine learning
        in gastroenterology. It should never replace clinical judgement.
    </div>
</div>
''', unsafe_allow_html=True)

section_divider()
show_disclaimer()
