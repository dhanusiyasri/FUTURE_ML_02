import streamlit as st
import pandas as pd
import pickle

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Churn Prediction",
    page_icon="📉",
    layout="wide"
)

# =========================
# CUSTOM CSS (UI MAGIC)
# =========================
st.markdown("""
<style>
.main {
    background-color: #f5f7fb;
}
.header {
    background: linear-gradient(90deg, #4b6cb7, #182848);
    padding: 25px;
    border-radius: 12px;
    color: white;
    text-align: center;
}
.card {
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}
.metric-card {
    text-align: center;
    font-size: 22px;
}
</style>
""", unsafe_allow_html=True)

# =========================
# LOAD FILES
# =========================
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = pickle.load(open(os.path.join(BASE_DIR, "xgb_model.pkl"), "rb"))
scaler = pickle.load(open(os.path.join(BASE_DIR, "scaler.pkl"), "rb"))
columns = pickle.load(open(os.path.join(BASE_DIR, "model_columns.pkl"), "rb"))


# =========================
# HEADER
# =========================
st.markdown("""
<div class="header">
    <h1>📉 Customer Churn Prediction System</h1>
    <p>Predict churn probability & take proactive retention actions</p>
</div>
""", unsafe_allow_html=True)

st.write("")

# =========================
# MAIN LAYOUT
# =========================
left, right = st.columns([1.1, 1])

# =========================
# LEFT: INPUT PANEL
# =========================
with left:
    st.markdown("<div class='card'><h3>👤 Customer Details</h3>", unsafe_allow_html=True)

    tenure = st.slider("Tenure (months)", 0, 72, 12)
    monthly = st.slider("Monthly Charges ($)", 20, 150, 70)
    total = st.slider("Total Charges ($)", 0, 10000, 1500)

    contract = st.selectbox(
        "📄 Contract Type",
        ["Month-to-month", "One year", "Two year"]
    )

    internet = st.selectbox(
        "🌐 Internet Service",
        ["DSL", "Fiber optic", "No"]
    )

    payment = st.selectbox(
        "💳 Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )

    paperless = st.radio("🧾 Paperless Billing", ["Yes", "No"], horizontal=True)

    st.markdown("</div>", unsafe_allow_html=True)

# =========================
# BUILD FEATURE VECTOR
# =========================
input_df = pd.DataFrame(0, index=[0], columns=columns)

scaled_vals = scaler.transform([[tenure, monthly, total]])
input_df["tenure"] = scaled_vals[0][0]
input_df["MonthlyCharges"] = scaled_vals[0][1]
input_df["TotalCharges"] = scaled_vals[0][2]

if contract == "One year" and "Contract_One year" in columns:
    input_df["Contract_One year"] = 1
elif contract == "Two year" and "Contract_Two year" in columns:
    input_df["Contract_Two year"] = 1

if internet == "Fiber optic" and "InternetService_Fiber optic" in columns:
    input_df["InternetService_Fiber optic"] = 1
elif internet == "No" and "InternetService_No" in columns:
    input_df["InternetService_No"] = 1

pay_col = f"PaymentMethod_{payment}"
if pay_col in columns:
    input_df[pay_col] = 1

if paperless == "Yes" and "PaperlessBilling_Yes" in columns:
    input_df["PaperlessBilling_Yes"] = 1

# =========================
# RIGHT: OUTPUT PANEL
# =========================
with right:
    st.markdown("<div class='card'><h3>🔮 Prediction Result</h3>", unsafe_allow_html=True)

    prob = model.predict_proba(input_df)[0][1]
    percent = int(prob * 100)

    st.progress(percent)

    st.markdown(
        f"<div class='metric-card'><b>Churn Probability</b><br><h1>{percent}%</h1></div>",
        unsafe_allow_html=True
    )

    if prob > 0.7:
        st.error("🔴 High Risk of Churn")
        st.write("**Action:** Offer discounts or long-term contract incentives.")
    elif prob > 0.4:
        st.warning("🟠 Medium Risk of Churn")
        st.write("**Action:** Improve engagement & customer support.")
    else:
        st.success("🟢 Low Risk of Churn")
        st.write("**Action:** Focus on loyalty programs & upselling.")

    st.markdown("</div>", unsafe_allow_html=True)

# =========================
# FOOTER
# =========================
st.markdown("""
---
<center>
<b>Customer Churn Prediction</b> | Machine Learning Project  
Built using Python, XGBoost & Streamlit
</center>
""", unsafe_allow_html=True)
