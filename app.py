import streamlit as st
import pandas as pd
import joblib

# ------------------------------------------------------------
# Load model (cached so it only loads once)
# ------------------------------------------------------------
@st.cache_resource
def load_model():
    return joblib.load("gradient_boosting_model.pkl")

model = load_model()

# ------------------------------------------------------------
# Page setup
# ------------------------------------------------------------
st.set_page_config(page_title="Student Performance Predictor", page_icon="🎓")
st.title("🎓 Student Performance Predictor")
st.write("Enter the details below to predict the performance score.")

# ------------------------------------------------------------
# Input form
# ------------------------------------------------------------
hours_studied = st.number_input("Hours Studied", min_value=0, max_value=24, value=5)
previous_scores = st.number_input("Previous Scores", min_value=0, max_value=100, value=70)
extracurricular = st.selectbox("Extracurricular Activities", ["Yes", "No"])
sleep_hours = st.number_input("Sleep Hours", min_value=0, max_value=24, value=7)
papers_practiced = st.number_input("Sample Question Papers Practiced", min_value=0, max_value=20, value=5)

extracurricular_val = 1 if extracurricular == "Yes" else 0

if st.button("Predict Performance"):
    input_df = pd.DataFrame([{
        "Hours Studied": hours_studied,
        "Previous Scores": previous_scores,
        "Extracurricular Activities": extracurricular_val,
        "Sleep Hours": sleep_hours,
        "Sample Question Papers Practiced": papers_practiced,
    }])

    prediction = model.predict(input_df)[0]
    st.success(f"Predicted Performance Index: **{prediction}**")

    # Show class probabilities if available
    if hasattr(model, "predict_proba"):
        proba = model.predict_proba(input_df)[0]
        top5_idx = proba.argsort()[-5:][::-1]
        st.write("Top 5 most likely scores:")
        for idx in top5_idx:
            st.write(f"- {model.classes_[idx]:.0f} — {proba[idx]*100:.1f}% confidence")
