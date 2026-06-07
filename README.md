# Telecom Customer Churn Prediction

A small Streamlit app for predicting customer churn in a telecom dataset using a pre-trained machine learning model.

## Project Overview

This project provides an interactive web app that allows users to simulate customer profiles and predict whether a telecom customer is likely to churn. The app loads a saved model from `churn_model.pkl` and uses selected customer features to generate a churn prediction.

## Files

- `app.py` - Streamlit application code.
- `churn_model.pkl` - Pre-trained churn prediction model loaded by the app.
- `WA_Fn-UseC_-Telco-Customer-Churn.csv` - Original telecom customer churn dataset.
- `.gitignore` - Files and folders ignored by Git.

## Features

- Predicts churn based on customer profile inputs
- Supports key telecom features such as contract type, internet service, billing, and monthly charges
- Displays the input values and churn outcome clearly in the UI

## Installation

1. Install Python 3.8+.
2. Open a terminal in the project folder.
3. Install dependencies:

```bash
pip install streamlit pandas scikit-learn joblib
```

## Usage

1. Ensure `app.py`, `churn_model.pkl`, and the dataset file are in the same folder.
2. Run the Streamlit app:

```bash
streamlit run app.py
```

3. Use the UI to select customer features and click **Predict churn**.

## Input Fields

The app accepts the following customer profile inputs:

- `Contract` - Month-to-month, One year, Two year
- `tenure` - Number of months with the provider
- `MonthlyCharges` - Monthly bill amount
- `PaperlessBilling` - Yes or No
- `Dependents` - Yes or No
- `InternetService` - DSL, Fiber optic, No
- `OnlineSecurity` - Yes or No
- `OnlineBackup` - Yes or No
- `TechSupport` - Yes or No
- `StreamingTV` - Yes or No
- `StreamingMovies` - Yes or No

## Notes

- If `churn_model.pkl` is missing or cannot be loaded, the app will show an error and stop.
- The model was trained from the telecom churn dataset and expects the same feature names and categories.

## Extending the Project

To improve the project further, consider:

- Adding data preprocessing and training scripts
- Displaying feature importance or model confidence
- Improving the UI with additional customer details
- Packaging the app with a `requirements.txt` or `pyproject.toml`

## License

This project is provided as-is for demonstration and educational purposes.
