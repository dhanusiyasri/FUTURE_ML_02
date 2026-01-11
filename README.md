# 📉 Customer Churn Prediction System

## 📌 Project Overview

Customer churn refers to customers stopping the use of a company’s services. Predicting churn helps businesses take proactive steps to retain customers, which is more cost-effective than acquiring new ones.

This project implements an **end-to-end Customer Churn Prediction System** using machine learning. The system predicts **churn probability for each customer**, identifies **key churn drivers**, and presents insights through an **interactive Streamlit app** and a **Power BI dashboard**.

---

## 🎯 Project Objectives

* Predict customer churn probability using machine learning
* Identify key factors driving customer churn
* Segment customers into churn risk categories
* Present insights in a business-friendly dashboard
* Demonstrate deployment using a web interface

---

## 📂 Dataset

* **Dataset Name:** Telco Customer Churn Dataset
* **Source:** Public telecom customer dataset
* **Records:** ~7,000 customers
* **Target Variable:** `Churn` (Yes / No)

---

## 🛠️ Tools & Technologies Used

* **Python**
* **Pandas & NumPy** – Data manipulation
* **Scikit-learn** – Preprocessing & evaluation
* **XGBoost** – Churn prediction model
* **Matplotlib & Seaborn** – Visualization
* **Streamlit** – Interactive web application
* **Power BI** – Business analytics dashboard

---

## 🔄 Project Workflow

1. Data loading and exploration
2. Data cleaning and preprocessing
3. Feature encoding and scaling
4. Model training and evaluation
5. Churn probability prediction
6. Risk segmentation
7. Dashboard and UI development

---

## 🧠 Machine Learning Model

* **Model Used:** XGBoost Classifier
* **Why XGBoost?**

  * Handles complex feature interactions
  * Performs well on tabular data
  * Provides feature importance for explainability

---

## 📊 Model Evaluation

The model was evaluated using:

* Confusion Matrix
* Precision, Recall, F1-score
* ROC-AUC Score

These metrics ensure the model effectively identifies customers likely to churn.

---

## 🔑 Key Features Implemented

* ✔ Churn probability prediction per customer
* ✔ Feature importance analysis (churn drivers)
* ✔ Confusion matrix and performance metrics
* ✔ Customer risk segmentation (Low / Medium / High)
* ✔ Interactive Streamlit web application
* ✔ Power BI dashboard for business insights

---

## 🌐 Streamlit Web Application

The Streamlit app allows users to:

* Enter customer details
* View churn probability in real time
* See churn risk category
* Get recommended business actions

**Run the app:**

```bash
streamlit run app.py
```
 **Or
 Use this link:**
 https://telco-customer-churn-prediction-system-future-intern.streamlit.app/

---

## 📈 Power BI Dashboard

The Power BI dashboard includes:

* KPI cards (Churn Rate, Customers, Charges)
* Churn distribution visualization
* Contract-wise churn analysis
* Risk segmentation
* High-risk customer table
* Interactive slicers

---

## 📁 Project Structure

```
Customer-Churn-Prediction/
│
├── churn_prediction.ipynb
├── app.py
├── xgb_model.pkl
├── scaler.pkl
├── model_columns.pkl
├── churn_dashboard_data.csv
├── PowerBI_Dashboard.pbix
└── README.md
```

---

## 📌 Business Insights

* Month-to-month contract customers show higher churn
* Higher monthly charges increase churn risk
* Long-term contracts significantly reduce churn
* High-risk customers can be targeted for retention offers

---

## 🚀 Future Enhancements

* SHAP-based explainability
* Automated retraining pipeline
* Deployment on cloud platforms
* Integration with CRM systems

---
## 📬 Acknowledgment

This project was completed as part of Future Interns – Machine Learning Task 2, focusing on practical implementation of prediction and analysis concepts.

---

## 👤 Author

**Dhanusiya Sri M**

**Machine Learning Enthusiastic**

---
