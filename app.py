import streamlit as st

st.set_page_config(page_title="Car Price Prediction", page_icon=":car:", layout="wide")

st.title("Welcome to Car Price Prediction App")
st.markdown("""
This app helps you **predict the price of a used car** based on various features like make, Engine , year, mileage, and more.

Use the sidebar to navigate between:
- **Home** - You're here!
- **Info** - Learn about the data and features used.
- **Predict** - Enter car details and get the estimated price.
""")
