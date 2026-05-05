import os
import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Resolve paths relative to the project root
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


@st.cache_resource
def load_model():
    """Load the trained RandomForestClassifier (cached for performance)."""
    return joblib.load(os.path.join(PROJECT_ROOT, 'final_diagnosis_model.pkl'))


@st.cache_resource
def load_scaler():
    """Load the StandardScaler (cached for performance)."""
    return joblib.load(os.path.join(PROJECT_ROOT, 'scaler.pkl'))


@st.cache_resource
def load_label_encoder():
    """Load the LabelEncoder (cached for performance)."""
    return joblib.load(os.path.join(PROJECT_ROOT, 'label_encoder.pkl'))


# The 8 features the model was trained on (in order)
FEATURE_NAMES = [
    'Age',
    'Baseline H₂ (ppm)',
    'Baseline CH₄ (ppm)',
    'Peak H₂ (ppm)',
    'Peak CH₄ (ppm)',
    'Combined Peak (ppm)',
    'Time of Peak (minutes)',
    'Increase from Baseline (ppm)',
]

# Diagnosis colour mapping
DIAGNOSIS_COLORS = {
    'SIBO': '#38bdf8',
    'IMO': '#f59e0b',
    'SIBO & IMO': '#ef4444',
    'No Diagnosis': '#22c55e',
}


def predict_diagnosis(age, baseline_h2, baseline_ch4, peak_h2, peak_ch4,
                      combined_peak, time_of_peak, increase_from_baseline):
    """
    Run prediction and return the diagnosis label, probabilities dict,
    and the raw input DataFrame.
    """
    model = load_model()
    scaler = load_scaler()
    le = load_label_encoder()

    input_data = pd.DataFrame({
        'Age': [age],
        'Baseline H₂ (ppm)': [baseline_h2],
        'Baseline CH₄ (ppm)': [baseline_ch4],
        'Peak H₂ (ppm)': [peak_h2],
        'Peak CH₄ (ppm)': [peak_ch4],
        'Combined Peak (ppm)': [combined_peak],
        'Time of Peak (minutes)': [time_of_peak],
        'Increase from Baseline (ppm)': [increase_from_baseline],
    })

    scaled_data = scaler.transform(input_data)
    prediction = model.predict(scaled_data)
    probabilities = model.predict_proba(scaled_data)[0]

    diagnosis = le.inverse_transform(prediction)[0]
    class_names = le.classes_

    prob_dict = {name: float(prob) * 100 for name, prob in zip(class_names, probabilities)}

    return diagnosis, prob_dict, input_data


def get_feature_importance():
    """Extract feature importance scores from the RandomForest model."""
    model = load_model()
    importances = model.feature_importances_
    return dict(zip(FEATURE_NAMES, importances))


def get_clinical_interpretation(diagnosis, input_values):
    """
    Generate rule-based clinical interpretation text.
    input_values is a dict with the raw (unscaled) feature values.
    """
    lines = []
    peak_h2 = input_values.get('Peak H₂ (ppm)', 0)
    peak_ch4 = input_values.get('Peak CH₄ (ppm)', 0)
    baseline_h2 = input_values.get('Baseline H₂ (ppm)', 0)
    baseline_ch4 = input_values.get('Baseline CH₄ (ppm)', 0)
    increase = input_values.get('Increase from Baseline (ppm)', 0)
    time_peak = input_values.get('Time of Peak (minutes)', 0)
    combined = input_values.get('Combined Peak (ppm)', 0)

    h2_rise = peak_h2 - baseline_h2

    # H2 analysis
    if h2_rise >= 20:
        lines.append(f"📈 **Hydrogen rise of {h2_rise:.0f} ppm** exceeds the ≥20 ppm threshold, "
                      "indicating significant hydrogen production by small-intestinal bacteria.")
    else:
        lines.append(f"📉 Hydrogen rise of {h2_rise:.0f} ppm is below the 20 ppm diagnostic threshold.")

    # CH4 analysis
    if peak_ch4 >= 10:
        lines.append(f"📈 **Methane level of {peak_ch4:.0f} ppm** meets or exceeds the ≥10 ppm threshold, "
                      "consistent with methanogen overgrowth (IMO).")
    else:
        lines.append(f"📉 Methane level of {peak_ch4:.0f} ppm is below the 10 ppm IMO threshold.")

    # Time analysis
    if time_peak <= 90:
        lines.append(f"⏱️ Peak at **{time_peak:.0f} minutes** suggests possible proximal small bowel involvement.")
    else:
        lines.append(f"⏱️ Peak at **{time_peak:.0f} minutes** is within the typical substrate transit time range.")

    # Combined peak
    if combined >= 30:
        lines.append(f"⚡ Combined peak of **{combined:.0f} ppm** is notably elevated, "
                      "suggesting significant overall bacterial gas production.")

    # Diagnosis summary
    if diagnosis == 'SIBO':
        lines.append("\n🔵 **Interpretation:** Pattern consistent with **hydrogen-dominant SIBO**. "
                      "Elevated H₂ without significant CH₄ suggests bacterial overgrowth "
                      "producing primarily hydrogen gas.")
    elif diagnosis == 'IMO':
        lines.append("\n🟠 **Interpretation:** Pattern consistent with **Intestinal Methanogen Overgrowth (IMO)**. "
                      "Elevated CH₄ levels indicate archaeal methanogen overgrowth, "
                      "which can be present throughout the GI tract.")
    elif diagnosis == 'SIBO & IMO':
        lines.append("\n🔴 **Interpretation:** Pattern consistent with **combined SIBO and IMO**. "
                      "Both hydrogen and methane are significantly elevated, "
                      "indicating mixed bacterial and methanogen overgrowth.")
    else:
        lines.append("\n🟢 **Interpretation:** Gas levels are within normal parameters. "
                      "No significant evidence of SIBO or IMO based on the breath test values provided.")

    return "\n\n".join(lines)


# Reference ranges for educational display
REFERENCE_RANGES = {
    'Baseline H₂ (ppm)': {'normal': '0–10', 'elevated': '> 10', 'note': 'Fasting hydrogen level'},
    'Baseline CH₄ (ppm)': {'normal': '0–5', 'elevated': '> 5', 'note': 'Fasting methane level'},
    'Peak H₂ (ppm)': {'normal': '< 20 above baseline', 'elevated': '≥ 20 above baseline', 'note': 'SIBO indicator'},
    'Peak CH₄ (ppm)': {'normal': '< 10', 'elevated': '≥ 10', 'note': 'IMO indicator'},
    'Combined Peak (ppm)': {'normal': '< 30', 'elevated': '≥ 30', 'note': 'Total gas production'},
    'Time of Peak (minutes)': {'normal': '90–120', 'elevated': '< 90 (early)', 'note': 'Transit time marker'},
    'Increase from Baseline (ppm)': {'normal': '< 20', 'elevated': '≥ 20', 'note': 'Rise from baseline'},
}


def store_patient_in_session(patient_name, gender, input_values, diagnosis, probabilities):
    """Store a patient's data in session state for comparison and report export."""
    if 'current_patient' not in st.session_state:
        st.session_state.current_patient = {}

    st.session_state.current_patient = {
        'name': patient_name,
        'gender': gender,
        'inputs': input_values,
        'diagnosis': diagnosis,
        'probabilities': probabilities,
    }


def add_patient_to_comparison(patient_data):
    """Add a patient dict to the comparison list in session state."""
    if 'patients_list' not in st.session_state:
        st.session_state.patients_list = []

    st.session_state.patients_list.append(patient_data)
