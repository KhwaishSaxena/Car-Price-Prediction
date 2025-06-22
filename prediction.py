import streamlit as st
import numpy as np
import pickle

# Load model, scaler, encoder
model = pickle.load(open("xgboost_model.pkl", "rb"))


color_encoder = pickle.load(open("color_encoder.pkl", "rb"))
drivetrain_encoder = pickle.load(open("drivetrain_encoder.pkl", "rb"))
fuel_encoder = pickle.load(open("fuel_encoder.pkl", "rb"))
location_encoder = pickle.load(open("location_encoder.pkl", "rb"))
make_encoder = pickle.load(open("make_encoder.pkl", "rb"))
owner_encoder = pickle.load(open("owner_encoder.pkl", "rb"))
seller_encoder = pickle.load(open("seller_encoder.pkl", "rb"))
transmission_encoder = pickle.load(open("transmission_encoder.pkl", "rb"))

st.title("Car Price Prediction")

# Input features using encoder classes for dropdowns
make = st.selectbox("Make", make_encoder.classes_)
fuel_type = st.selectbox("Fuel Type", fuel_encoder.classes_)
owner = st.selectbox("Owner", owner_encoder.classes_)
drivetrain = st.selectbox("Drivetrain", drivetrain_encoder.classes_)
transmission = st.selectbox("Transmission", transmission_encoder.classes_)
seller_type = st.selectbox("Seller Type", seller_encoder.classes_)
color = st.selectbox("Color", color_encoder.classes_)
Loc = st.selectbox("Location", location_encoder.classes_)

year = st.number_input("Year", min_value=1990, max_value=2050, format="%d")
km = st.number_input("Kilometers Driven", min_value=0, format="%d")
engine = st.number_input("Engine (in CC)", min_value=0, format="%d")
sc = st.slider("Seating Capacity", min_value=4, max_value=7)
fc = st.number_input("Full Tank Capacity (Litres)", min_value=0, format="%d")

with st.expander("Engine Specifications"):
    power_bhp = st.number_input("Power (BHP)", min_value=20, max_value=1000, format="%d")
    power_rpm = st.number_input("Power RPM", min_value=1000, max_value=8000, format="%d")
    torque_nm = st.number_input("Torque (Nm)", min_value=30, max_value=1000, format="%d")
    torque_rpm = st.number_input("Torque RPM", min_value=1000, max_value=8000, format="%d")

with st.expander("Car Dimensions"):
    length = st.number_input("Length (mm)", min_value=0, format="%d")
    width = st.number_input("Width (mm)", min_value=0, format="%d")
    height = st.number_input("Height (mm)", min_value=0, format="%d")

# Encode categorical features
try:
    make_enc = make_encoder.transform([make])[0]
    fuel_enc = fuel_encoder.transform([fuel_type])[0]
    owner_enc = owner_encoder.transform([owner])[0]
    drive_enc = drivetrain_encoder.transform([drivetrain])[0]
    trans_enc = transmission_encoder.transform([transmission])[0]
    seller_enc = seller_encoder.transform([seller_type])[0]
    color_enc = color_encoder.transform([color])[0]
    loc_enc = location_encoder.transform([Loc])[0]
except Exception as e:
    st.error("Encoding failed. Please check your encoder.pkl file.")
    st.exception(e)
    st.stop()

# Final input array
input_array = np.array([[make_enc, year, km, fuel_enc, trans_enc, loc_enc, color_enc, owner_enc,
                         seller_enc, engine, drive_enc, length, width, height, sc, fc, power_bhp,
                         power_rpm, torque_nm, torque_rpm]] )

print(input_array)

# Predict
if st.button("Predict Price"):
    try:
        pred = model.predict(input_array)[0]
        st.success(f"Estimated Car Price: ₹{pred} Lakhs")
    except Exception as e:
        st.error("Prediction failed. Please check model or input compatibility.")
        st.exception(e)

