
# 🌍 Carbon Emission Prediction using Machine Learning

This project predicts country-specific **CO₂ emissions** using key economic and energy indicators through machine learning models. The goal is to help policymakers, analysts, and researchers estimate emissions based on historical and current data.

---

## 🚀 Features

- ✅ Predict CO₂ Emissions based on:
  - GDP
  - Population
  - Energy Use
  - Energy per GDP
  - FDI (% of GDP)
  - Cereal Yield
  - Protected Area (%)
- ✅ Interactive Streamlit Web App
- ✅ Batch prediction via Excel upload
- ✅ Visualizations of inputs and prediction results
- ✅ Model trained with Random Forest Regressor
- ✅ Fully containerized and deployable (Streamlit Cloud, Render, etc.)

---

## 📁 Folder Structure

```

carbon_emission_prediction/
│
├── app.py # Streamlit web app
├── models/
│ └── emission_model.pkl # Trained ML model
├── data/
│ └── climate_change.xls # Raw dataset
├── src/
│ ├── load_data.py
│ ├── preprocess.py
│ └── model.py
├── requirements.txt
└── README.md

```

---

## 🧠 Model & Dataset

- ✅ Model: `RandomForestRegressor`
- ✅ Dataset: Climate Change Data from [World Bank / Kaggle](https://data.worldbank.org)
- ✅ Input Features (7):
  - `gdp`
  - `pop`
  - `en_per_cap`
  - `en_per_gdp`
  - `fdi_perc_gdp`
  - `cereal_yield`
  - `prot_area_perc`

---

## 📦 Installation

```bash
# Clone the repo
git clone https://github.com/Yogeshwarypl/Carbon_Emission_Pred_Complete_Model.git
cd carbon-emission-predictor

# Create a virtual environment
python -m venv .venv
source .venv/bin/activate    # or .venv\Scripts\activate on Windows

#Install dependencies
pip install -r requirements.txt

```
##🎯 Run the App
```

streamlit run app.py

```
You can now access the app at http://localhost:8501

---
##📈 Future Enhancements
🔄 Add time-series forecasting (Prophet, ARIMA)

🧠 Integrate SHAP explainability

🌍 Live data scraping from World Bank APIs

📥 PDF report generation

---

🤝 Contributions
Contributions and pull requests are welcome! Please open an issue first for major changes.

📜 License
This project is licensed under the MIT License.


---

