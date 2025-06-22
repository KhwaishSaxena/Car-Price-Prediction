import streamlit as st
import numpy as np
import pickle

# Load model, scaler, encoder
model = pickle.load(open("xgboost_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

encoder = pickle.load(open("encoder.pkl", "rb"))

st.title("Car Price Prediction")

# Input features using encoder classes for dropdowns
make = st.selectbox("Make", encoder['make'].classes_)
fuel_type = st.selectbox("Fuel Type", encoder['fuel_type'].classes_)
owner = st.selectbox("Owner", encoder['owner'].classes_)
drivetrain = st.selectbox("Drivetrain", encoder['drivetrain'].classes_)
transmission = st.selectbox("Transmission", encoder['transmission'].classes_)
seller_type = st.selectbox("Seller Type", encoder['seller_type'].classes_)
color = st.selectbox("Color", encoder['color'].classes_)
Loc = st.selectbox("Location", encoder['location'].classes_)

year = st.number_input("Year", min_value=1990, max_value=2050, format="%d")
km = st.number_input("Kilometers Driven", min_value=0, format="%d")
engine = st.number_input("Engine (in CC)", min_value=0, format="%d")
sc = st.slider("Seating Capacity", min_value=4, max_value=7)
fc = st.number_input("Full Tank Capacity (Litres)", min_value=0, format="%d")

with st.expander("Engine Specifications"):
    power_bhp = st.slider("Power (BHP)", 20, 1000)
    power_rpm = st.slider("Power RPM", 1000, 8000)
    torque_nm = st.slider("Torque (Nm)", 30, 1000)
    torque_rpm = st.slider("Torque RPM", 1000, 8000)

with st.expander("Car Dimensions"):
    length = st.number_input("Length (mm)", min_value=0, format="%d")
    width = st.number_input("Width (mm)", min_value=0, format="%d")
    height = st.number_input("Height (mm)", min_value=0, format="%d")

# Encode categorical features
try:
    make_enc = encoder['make'].transform([make])[0]
    fuel_enc = encoder['fuel_type'].transform([fuel_type])[0]
    owner_enc = encoder['owner'].transform([owner])[0]
    drive_enc = encoder['drivetrain'].transform([drivetrain])[0]
    trans_enc = encoder['transmission'].transform([transmission])[0]
    seller_enc = encoder['seller_type'].transform([seller_type])[0]
    color_enc = encoder['color'].transform([color])[0]
    loc_enc = encoder['location'].transform([Loc])[0]
except Exception as e:
    st.error("Encoding failed. Please check your encoder.pkl file.")
    st.exception(e)
    st.stop()

# Final input array
input_array = np.array([[make_enc, fuel_enc, owner_enc, drive_enc, trans_enc, seller_enc, loc_enc, color_enc,
                         year, km, fc, sc, engine, power_bhp, power_rpm, torque_nm, torque_rpm,
                         length, width, height]])

# Scale features
try:
    input_scaled = scaler.transform(input_array)
except Exception as e:
    st.error("Scaling failed. Please check your scaler.pkl file.")
    st.exception(e)
    st.stop()

# Predict
if st.button("Predict Price"):
    try:
        price_lakh = model.predict(input_scaled)[0]
        price_rupees = price_lakh * 1000
        st.success(f"Estimated Car Price: ₹ {price_rupees}")
    except Exception as e:
        st.error("Prediction failed. Please check model or input compatibility.")
        st.exception(e)

