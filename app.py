import streamlit as st
import joblib
import pandas as pd

st.set_page_config(page_title="Telecom Customer Churn Prediction", page_icon="📞")
st.title("Telecom Customer Churn Prediction")


try:
    model = joblib.load("churn_model.pkl")
except Exception:
    st.error("Cannot load churn_model.pkl. Put the file in the same folder as app.py.")
    st.stop()

col1, col2 = st.columns(2)
with col1:
    Contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    tenure = st.number_input("Tenure (months)", min_value=0, max_value=100, value=12)
    MonthlyCharges = st.number_input("Monthly charges", min_value=0.0, value=70.0)
    PaperlessBilling = st.selectbox("Paperless billing", ["Yes", "No"])
    Dependents = st.selectbox("Dependents", ["Yes", "No"])

with col2:
    InternetService = st.selectbox("Internet service", ["DSL", "Fiber optic", "No"])
    OnlineSecurity = st.selectbox("Online security", ["Yes", "No "])
    OnlineBackup = st.selectbox("Online backup", ["Yes", "No "])
    TechSupport = st.selectbox("Tech support", ["Yes", "No "])
    StreamingTV = st.selectbox("Streaming TV", ["Yes", "No "])
    StreamingMovies = st.selectbox("Streaming movies", ["Yes", "No "])

if st.button("Predict churn"):
    data = pd.DataFrame([
        {
            "Dependents": Dependents,
            "tenure": tenure,
            "InternetService": InternetService,
            "OnlineSecurity": OnlineSecurity,
            "OnlineBackup": OnlineBackup,
            "TechSupport": TechSupport,
            "StreamingTV": StreamingTV,
            "StreamingMovies": StreamingMovies,
            "Contract": Contract,
            "PaperlessBilling": PaperlessBilling,
            "MonthlyCharges": MonthlyCharges,
        }
    ])

    prediction = model.predict(data)[0]
    if prediction == 1:
        st.error("Customer is likely to churn." \
        " Consider offering discounts or improving service quality.")
    else:
        st.success("Customer is likely to stay." \
        " Continue providing excellent service to retain them.")

    st.write("### Input values")
    st.dataframe(data)
