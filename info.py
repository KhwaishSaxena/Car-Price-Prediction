import streamlit as st

st.title("About Car Price Prediction Project")
st.write("""
        ## Objective
    The primary goal of this project is to leverage machine learning to accurately predict the **resale value of cars** based on various attributes. This assists buyers, sellers, and dealerships in making **data-driven decisions** when evaluating vehicle prices.
    
    By analyzing features such as brand, model year, fuel type, transmission, mileage, and ownership history, the model provides a reliable prediction of the car's price in the current market.

    ---

    ## Dataset
    The model is trained on a publicly available **car dataset**, which includes features like:
    - Car Name / Brand
    - Year of Manufacture
    - Fuel Type
    - Transmission Type
    - Mileage (KM Driven)
    - Number of Previous Owners
    - Selling Price (Target variable)

    The dataset was cleaned, transformed, and split for training and evaluation. The final model was selected based on metrics such as **R² score**, **RMSE**, and **MAE**, ensuring accurate and trustworthy predictions.

    ---

    ##  Technologies Used
    - **Python**: For data analysis and model development.
    - **Pandas & NumPy**: For data manipulation and preprocessing.
    - **Scikit-learn**: For model training, evaluation, and pipeline creation.
    - **Matplotlib & Seaborn**: For data visualization and insights.
    - **Streamlit**: To build an interactive and easy-to-use web app for users.

    ---

     *Built using Machine Learning and Streamlit for Real-World Application.*

        """)

