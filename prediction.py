import streamlit as st
import pandas as pd
import numpy as np
import pickle
import xgboost as xgb
import os
model = pickle.load(open("xgboost_model.pkl", "rb"))
st.title('Car Price Prediction')

make_mapping = {k: i for i, k in enumerate(['Honda', 'Maruti Suzuki', 'Hyundai', 'Toyota', 'Mercedes-Benz', 'BMW', 'Skoda', 'Nissan', 'Renault', 'Tata', 'Volkswagen', 'Ford', 'Audi', 'Mahindra', 'MG', 'Jeep', 'Porsche', 'Kia', 'Land Rover', 'Volvo', 'Maserati', 'Jaguar', 'Isuzu', 'Fiat', 'MINI', 'Ferrari', 'Mitsubishi', 'Datsun', 'Lamborghini', 'Chevrolet', 'Ssangyong', 'Rolls-Royce', 'Lexus'])}
fuel_mapping = {k: i for i, k in enumerate(["Petrol", "Diesel", "CNG", "Others", "Electric"])}
owner_mapping = {k: i for i, k in enumerate(['First', 'Second', '3 or More', 'UnRegistered Car'])}
drive_mapping = {k: i for i, k in enumerate(['FWD', 'RWD', 'AWD'])}
trans_mapping = {k: i for i, k in enumerate(['Manual', 'Automatic'])}
seller_mapping = {k: i for i, k in enumerate(['Individual', 'Corporate', 'Commercial Registration'])}
color_mapping = {k: i for i, k in enumerate(['White', 'Silver', 'Blue', 'Black', 'Grey', 'Red', 'Others'])}
location_mapping = {k: i for i, k in enumerate(['Mumbai', 'Delhi', 'Bangalore', 'Hyderabad', 'Chandigarh', 'Lucknow', 'Kolkata', 'Ahmedabad', 'Patna', 'Chennai', 'Jaipur', 'Others'])}

# Apply the encodings
make = make_mapping[make]
fuel_type = fuel_mapping[fuel_type]
owner = owner_mapping[owner]
drivetrain = drive_mapping[drivetrain]
transmission = trans_mapping[transmission]
seller_type = seller_mapping[seller_type]
color = color_mapping[color]
Loc = location_mapping[Loc]
year = st.number_input("Year", min_value = 1990, format = "%d", help = "Manufacturing Year of the car")
km = st.number_input("Kilometers", min_value = 0, format = "%d", help = "Total kilometers Driven")
engine = st.number_input("Engine", min_value = 0, format = "%d", help = "engine capacity of the car in cc")
sc = st.slider("Seating Capacity", min_value=4, max_value=7,help = "Maximum people that can fir in a car")

fc = st.number_input("Full Tank Capacity", min_value = 0, format = "%d", help = "Maximum fuel capacity of the car in litres")

with st.expander("Engine Specifications"):
    power_bhp = st.slider("Power (BHP)", 20, 700, 120, 5)
    power_rpm = st.slider("Power RPM", 1000, 8000, 4000, 100)
    torque_nm = st.slider("Torque (Nm)", 30, 1000, 200, 10)
    torque_rpm = st.slider("Torque RPM", 1000, 8000, 4000, 100)
with st.expander("Car Dimensions"):
    length = st.number_input("Length", min_value = 0, format = "%d", help = "length of the car in mm")
    width = st.number_input("Width", min_value = 0, format = "%d", help = "width of the car in mm")
    height = st.number_input("Height", min_value = 0, format = "%d", help = "height of the car in mm")

if st.button("Predict"):
    input_array = np.array([[make, fuel_type, owner, drivetrain, transmission, seller_type,Loc, color, year, km, fc, sc, engine, power_bhp, power_rpm, torque_nm, torque_rpm, length, width, height]])

    def predict(input_array):
        price = model.predict(input_array)
        st.success(f"Estimated Car Price: ₹ {price:,.2f}")

    predict(input_array)

if __name__ == '__page__':
    predict()
