# Car Price Prediction Using Machine Learning

A Machine Learning-based web application that estimates the resale value of a car based on various features such as brand, fuel type, location, engine specs, and more. The app uses an XGBoost model with Optuna-based hyperparameter tuning for optimal performance.

**Kaggle Notebook:** [View Full Project Here](https://www.kaggle.com/code/khwaishsaxena/car-price-prediction)


## Overview

The aim of this project is to build an intelligent system that can predict the **resale price of a car** using supervised machine learning. The dataset includes various categorical and numerical features like Make, Fuel Type, Engine Power, Torque, and more.

The model was trained using **XGBoost Regressor**, with preprocessing including:
- Label encoding of categorical features


## Features

- Predict car resale price in lakhs 
- Label encoding of categorical columns
- Advanced feature engineering for power, torque, etc.
- Optuna used for hyperparameter optimization
- Web deployment using **Streamlit**

##  Machine Learning Workflow

1. **Data Preprocessing**
2. **Exploratory Data Analysis (EDA)**
3. **Model Building**
4. **Hyperparameter Optimization using Optuna**
5. **Model Evaluation**
6. **Deployment with Streamlit**


## Model Performance 

| Metric                        | Value               |
|------------------------------|---------------------|
| **Mean Absolute Error (MAE)**| ₹2.52 Lakhs         |
| **R² Score**                 | 0.92076 (92.07%)    |

 **Interpretation**:
- **MAE ≈ ₹2.5L** means that on average, your predictions are off by around ₹2.5 lakhs.
- **R² Score ≈ 92%** indicates your model explains 92% of the variance in the target variable (Price).
- Some variation (e.g., 1.5–2L mismatch) is **normal in real-world data**, especially for domains like car pricing where features can’t capture all pricing factors (e.g., physical condition, brand prestige, negotiability).


## Tech Stack

- **Python**
- **Pandas**, **NumPy**, **Matplotlib**, **Seaborn**
- **Scikit-learn**
- **XGBoost**, **Optuna**
- **Streamlit** for web UI
- **Label Encoding**
- **Pickle** for model serialization


##  How to Run This Project

```bash
# Step 1: Clone the repo
git clone https://github.com/KhwaishSaxena/Car-Price-Prediction
cd car-price-prediction

# Step 2: Install Requirements
pip install -r requirements.txt

# Step 3: Launch Streamlit App
streamlit run app.py
```
## Live Demo

[Car Price Estimator App](https://car-price-prediction-using-ml.streamlit.app/)
