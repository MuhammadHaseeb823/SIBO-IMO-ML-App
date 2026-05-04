import streamlit as st
import pandas as pd
import joblib

# Load the saved model, scaler, and label encoder
model = joblib.load('final_diagnosis_model.pkl')       # Classifier model
scaler = joblib.load('scaler.pkl')                     # Scaler for normalization
label_encoder = joblib.load('label_encoder.pkl')       # Label encoder for target

# Streamlit app title
st.title('SIBO & IMO Prediction App')

# Input fields for user to provide feature values
age = st.number_input('Age', min_value=0, max_value=120, value=30, step=1)
gender = st.selectbox('Gender', options=['M', 'F'])
baseline_h2 = st.number_input('Baseline H₂ (ppm)', min_value=0.0, value=5.0, step=0.1)
baseline_ch4 = st.number_input('Baseline CH₄ (ppm)', min_value=0.0, value=2.0, step=0.1)
peak_h2 = st.number_input('Peak H₂ (ppm)', min_value=0.0, value=74.0, step=0.1)
peak_ch4 = st.number_input('Peak CH₄ (ppm)', min_value=0.0, value=21.0, step=0.1)
combined_peak = st.number_input('Combined Peak (ppm)', min_value=0.0, value=95.0, step=0.1)
time_of_peak = st.number_input('Time of Peak (minutes)', min_value=0.0, value=100.0, step=0.1)
increase_from_baseline = st.number_input('Increase from Baseline (ppm)', min_value=0.0, value=90.0, step=0.1)

# Prediction button
if st.button('Predict Final Diagnosis'):
    # Create a DataFrame with the input data
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
    
    # One-hot encode the 'Gender' column
    # input_data = pd.get_dummies(input_data, columns=['Gender'], drop_first=True)
    
    # Add additional categorical variables here if necessary
    # For example: Combined Diagnosis, IMO, SIBO

    # # Ensure all expected features are present
    # # Get the feature names that the model was trained on
    # trained_features = model.feature_names_in_

    # # Add missing columns with default value of 0
    # for feature in trained_features:
    #     if feature not in input_data.columns:
    #         input_data[feature] = 0

    # # Reorder the input data to match the trained feature order
    # input_data = input_data[trained_features]

    # Standardize the input data using the saved scaler
    scaled_data = scaler.transform(input_data)
    # input_data['Gender_M'] = [1 if gender == 'M' else 0]  # Create Gender_M column
    print(input_data.columns)

    # Make predictions using the loaded model
    prediction = model.predict(scaled_data)

    # Decode the prediction
    final_diagnosis = label_encoder.inverse_transform(prediction)

    # Display the prediction
    st.write(f'The predicted final diagnosis is: **{final_diagnosis[0]}**')
