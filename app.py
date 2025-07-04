import streamlit as st
import joblib
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Load model
model = joblib.load("models/forecasting_co2_emmision.pkl")

st.set_page_config(page_title="Carbon Emission Prediction", layout="centered")
st.title("🌍 Carbon Emission Predictor")

st.markdown("Enter the values for the following indicators to predict total CO₂ emissions (in metric tons).")

with st.form("manual_input"):
    gdp = st.number_input("GDP (in USD)", min_value=0.0, step=0.1)
    pop = st.number_input("Population", min_value=0.0, step=0.1)
    en_per_cap = st.number_input("Energy use per capita", min_value=0.0, step=1.0)
    en_per_gdp = st.number_input("Energy use per unit GDP", min_value=0.0, step=0.1)
    fdi_perc_gdp = st.number_input("FDI (% of GDP)", min_value=0.0, step=0.1)
    cereal_yield = st.number_input("Cereal yield", min_value=0.0, step=0.1)
    prot_area_perc = st.number_input("Protected areas (%)", min_value=0.0, step=0.1)

    submit = st.form_submit_button("Predict Emission")

if submit:
    try:
        input_data = np.array([[gdp, pop, en_per_cap, en_per_gdp, fdi_perc_gdp, cereal_yield, prot_area_perc]])
        prediction = model.predict(input_data)
        st.success(f"🌱 Predicted CO₂ Emission: {prediction[0]:,.2f} metric tons")

        # Feature bar chart
        st.subheader("🔍 Feature Overview")
        feature_labels = ['GDP', 'Population', 'Energy/Capita', 'Energy/GDP', 'FDI %', 'Cereal Yield', 'Protected Area %']
        values = [gdp, pop, en_per_cap, en_per_gdp, fdi_perc_gdp, cereal_yield, prot_area_perc]
        feature_df = pd.DataFrame({'Feature': feature_labels, 'Value': values})
        fig, ax = plt.subplots()
        sns.barplot(data=feature_df, x='Feature', y='Value', ax=ax)
        plt.xticks(rotation=30)
        st.pyplot(fig)

    except Exception as e:
        st.error(f"Prediction Error: {e}")


