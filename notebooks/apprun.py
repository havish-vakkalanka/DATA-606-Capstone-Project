import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load the trained model and encoders
model = joblib.load("final_rf_model_top10.pkl")
sport_encoder = joblib.load("sport_encoder.pkl")
country_noc_encoder = joblib.load("country_noc_encoder.pkl")

# Retrieve class names from encoders
sport_classes = sport_encoder.classes_
country_classes = country_noc_encoder.classes_

# Streamlit App
st.title("Olympic Medal Count Prediction")
st.write("Input the details below:")

# Inputs
athlete_count = st.number_input("Number of Athletes", min_value=0, value=10, step=1)
country_name = st.selectbox("Country Name", country_classes)
average_height = st.number_input("Average Height (cm)", min_value=0.0, value=175.0, step=0.1)
average_age = st.number_input("Average Age", min_value=0.0, value=25.0, step=0.1)
sport_name = st.selectbox("Sport Name", ["All Sports"] + list(sport_classes))
average_weight = st.number_input("Average Weight (kg)", min_value=0.0, value=70.0, step=0.1)
team_sport_count = st.number_input("Team Sport Count", min_value=0, value=1, step=1)
gdp_per_capita = st.number_input("GDP per Capita", min_value=0.0, value=50000.0, step=100.0)
event_count = st.number_input("Event Count", min_value=0, value=30, step=1)
year_of_olympics = st.number_input("Year of the Olympics", min_value=1896, value=2024, step=1, max_value=2100)

# Encode categorical inputs
country_encoded = list(country_classes).index(country_name)
sport_encoded = -1 if sport_name == "All Sports" else list(sport_classes).index(sport_name)

# Prepare input data for the model
input_data = np.array([[
    athlete_count,
    country_encoded,
    average_height,
    average_age,
    sport_encoded if sport_name != "All Sports" else 0,  # Default sport encoding for "All Sports"
    average_weight,
    team_sport_count,
    gdp_per_capita,
    event_count,
    year_of_olympics
]])

# Prediction
if st.button("Predict Medal Count"):
    try:
        prediction = model.predict(input_data)[0]
        st.success(f"Predicted Medal Count: {round(prediction)}")
    except Exception as e:
        st.error(f"Error during prediction: {e}")
