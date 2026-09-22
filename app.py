import joblib
import numpy as np
import pandas as pd
import streamlit as st

# Set page title and layout
st.set_page_config(page_title="Drug Classification App", layout="centered")

st.title("💊 Clinical Drug Prescription Predictor")
st.write(
    "Enter patient vitals and lab metrics below to predict the recommended drug."
)


# Load the saved model pipeline
@st.cache_resource
def load_pipeline():
  return joblib.load("drug_classifier_pipeline.pkl")


try:
  pipeline = load_pipeline()
  model = pipeline["model"]
  le = pipeline["label_encoder"]
except Exception as e:
  st.error(
      f"Could not load 'drug_classifier_pipeline.pkl'. Make sure the file is in this folder. Details: {e}"
  )
  st.stop()

# Layout inputs into two columns
col1, col2 = st.columns(2)

with col1:
  age = st.slider("Patient Age", min_value=10, max_value=90, value=35, step=1)
  sex = st.selectbox("Sex", options=["M", "F"])
  bp = st.selectbox(
      "Blood Pressure (BP)", options=["HIGH", "NORMAL", "LOW"], index=1
  )

with col2:
  cholesterol = st.selectbox(
      "Cholesterol Level", options=["HIGH", "NORMAL"], index=1
  )
  na_to_k = st.slider(
      "Na_to_K Ratio", min_value=5.0, max_value=40.0, value=15.5, step=0.1
  )

# Encodings matching training phase
bp_map = {"LOW": 0, "NORMAL": 1, "HIGH": 2}
chol_map = {"NORMAL": 0, "HIGH": 1}
sex_map = {"F": 0, "M": 1}

# Predict button
if st.button("Predict Recommended Drug", type="primary"):
  input_data = pd.DataFrame([{
      "Age": age,
      "Sex": sex_map[sex],
      "BP": bp_map[bp],
      "Cholesterol": chol_map[cholesterol],
      "Na_to_K": na_to_k,
  }])

  # Run inference
  prediction_idx = model.predict(input_data)[0]
  probabilities = model.predict_proba(input_data)[0]
  predicted_drug = le.inverse_transform([prediction_idx])[0]

  st.success(f"**Recommended Prescription:** {predicted_drug}")
  st.metric(
      label="Prediction Confidence",
      value=f"{probabilities[prediction_idx] * 100:.1f}%",
  )

  # Display class probabilities chart
  st.subheader("Model Probabilities by Drug Class")
  prob_df = pd.DataFrame({
      "Drug": le.classes_,
      "Probability (%)": [p * 100 for p in probabilities],
  }).set_index("Drug")

  st.bar_chart(prob_df)