# 💊 Clinical Drug Response Predictor

An interactive clinical decision-support tool and machine learning web application that predicts optimal drug prescriptions based on patient vitals and biomarker indicators.

🔗 **Live Demo:** [https://Saurovmitro18.github.io/drug-response-predictor
/](https://Saurovmitro18.github.io/drug-response-predictor
/)

---

## 📌 Project Overview

Prescribing appropriate therapeutics often depends on complex interactions between age, cardiovascular metrics, and metabolic markers. This project analyzes clinical and demographic features from the `drug200` dataset to build an interpretable multi-class classification model that maps patient profiles to 5 distinct drug categories (`DrugY`, `drugA`, `drugB`, `drugC`, `drugX`).

### Key Features
* **Interactive Clinical Dashboard:** Adjust continuous sliders and categorical switches for patient vitals with real-time inference.
* **Instant Cohort Presets:** Pre-configured clinical archetypes (e.g., Young High-BP, Elderly High-BP, High Na/K ratio) to test decision boundaries instantly.
* **Multi-Class Probability Distribution:** Visualizes confidence ratings across all potential therapeutics.
* **Auditable Decision Trace:** Step-by-step breakdown explaining the underlying clinical criteria used to select each drug.
* **Zero Dependencies / Serverless Deployment:** Runs entirely in the client's browser using React and Tailwind CSS via GitHub Pages.

---

## 📊 Dataset & Feature Architecture

Trained on the clinical **Drug Classification Dataset**, comprising 200 patient profiles:

| Feature | Type | Description / Range |
| :--- | :--- | :--- |
| `Age` | Numerical | Patient age (10 to 90 years) |
| `Sex` | Categorical | Biological sex (`M`, `F`) |
| `BP` | Categorical | Blood Pressure tier (`LOW`, `NORMAL`, `HIGH`) |
| `Cholesterol` | Categorical | Serum cholesterol level (`NORMAL`, `HIGH`) |
| `Na_to_K` | Numerical | Sodium-to-Potassium ratio in blood (5.0 to 40.0) |
| **`Drug` (Target)** | **Multi-class** | **5 Target Classes:** `DrugY`, `drugA`, `drugB`, `drugC`, `drugX` |

---

## 🔬 Clinical Decision Rules (Model Logic)

The model reproduces the following tree-based decision hierarchy:

1. **Rule 1 (Metabolic Marker):** If `Na_to_K > 15.0` $\rightarrow$ **DrugY** (High confidence).
2. **Rule 2 (Hypertension):** If `Na_to_K <= 15.0` and `BP == HIGH`:
   * If `Age <= 50` $\rightarrow$ **drugA**
   * If `Age > 50` $\rightarrow$ **drugB**
3. **Rule 3 (Hypotension & Lipids):** If `Na_to_K <= 15.0` and `BP == LOW`:
   * If `Cholesterol == HIGH` $\rightarrow$ **drugC**
   * If `Cholesterol == NORMAL` $\rightarrow$ **drugX**
4. **Rule 4 (Normotension):** If `Na_to_K <= 15.0` and `BP == NORMAL` $\rightarrow$ **drugX**

---

## 🛠️ Tech Stack

* **Front-End & UI:** React (ES6+), Tailwind CSS, Lucide Icons
* **Data Science & ML (Training Pipeline):** Python, Scikit-Learn, Pandas, NumPy, Joblib
* **Deployment:** GitHub Pages (Static hosting)

---
