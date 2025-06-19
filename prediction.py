import streamlit as st
import numpy as np
import pickle

model = pickle.load(open("xgboost_model.pkl", "rb"))
st.title("Car Price Prediction")

make = st.selectbox("Make", ['Honda', 'Maruti Suzuki', 'Hyundai', 'Toyota', 'Mercedes-Benz', 'BMW', 'Skoda', 'Nissan', 'Renault', 'Tata', 'Volkswagen', 'Ford', 'Audi', 'Mahindra', 'MG', 'Jeep', 'Porsche', 'Kia', 'Land Rover', 'Volvo', 'Maserati', 'Jaguar', 'Isuzu', 'Fiat', 'MINI', 'Ferrari', 'Mitsubishi', 'Datsun', 'Lamborghini', 'Chevrolet', 'Ssangyong', 'Rolls-Royce', 'Lexus'])
fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG", "Others", "Electric"])
owner = st.selectbox("Owner", ['First', 'Second', '3 or More', 'UnRegistered Car'])
drivetrain = st.selectbox("Drivetrain", ['FWD', 'RWD', 'AWD'])
transmission = st.selectbox("Transmission", ['Manual', 'Automatic'])
seller_type = st.selectbox("Seller Type", ['Individual', 'Corporate', 'Commercial Registration'])
color = st.selectbox("Color", ['White', 'Silver', 'Blue', 'Black', 'Grey', 'Red', 'Others'])
Loc = st.selectbox("Location", ['Mumbai', 'Delhi', 'Bangalore', 'Hyderabad', 'Chandigarh', 'Lucknow', 'Kolkata', 'Ahmedabad', 'Patna', 'Chennai', 'Jaipur', 'Others'])

year = st.number_input("Year", min_value=1990, format="%d")
km = st.number_input("Kilometers Driven", min_value=0, format="%d")
engine = st.number_input("Engine (in CC)", min_value=0, format="%d")
sc = st.slider("Seating Capacity", min_value=4, max_value=7)
fc = st.number_input("Full Tank Capacity (Litres)", min_value=0, format="%d")

with st.expander("Engine Specifications"):
    power_bhp = st.slider("Power (BHP)", 20, 700, 120, 5)
    power_rpm = st.slider("Power RPM", 1000, 8000, 4000, 100)
    torque_nm = st.slider("Torque (Nm)", 30, 1000, 200, 10)
    torque_rpm = st.slider("Torque RPM", 1000, 8000, 4000, 100)

with st.expander("Car Dimensions"):
    length = st.number_input("Length (mm)", min_value=0, format="%d")
    width = st.number_input("Width (mm)", min_value=0, format="%d")
    height = st.number_input("Height (mm)", min_value=0, format="%d")

make_mapping = {k: i for i, k in enumerate(['Honda', 'Maruti Suzuki', 'Hyundai', 'Toyota', 'Mercedes-Benz', 'BMW', 'Skoda', 'Nissan', 'Renault', 'Tata', 'Volkswagen', 'Ford', 'Audi', 'Mahindra', 'MG', 'Jeep', 'Porsche', 'Kia', 'Land Rover', 'Volvo', 'Maserati', 'Jaguar', 'Isuzu', 'Fiat', 'MINI', 'Ferrari', 'Mitsubishi', 'Datsun', 'Lamborghini', 'Chevrolet', 'Ssangyong', 'Rolls-Royce', 'Lexus'])}
fuel_mapping = {k: i for i, k in enumerate(["Petrol", "Diesel", "CNG", "Others", "Electric"])}
owner_mapping = {k: i for i, k in enumerate(['First', 'Second', '3 or More', 'UnRegistered Car'])}
drive_mapping = {k: i for i, k in enumerate(['FWD', 'RWD', 'AWD'])}
trans_mapping = {k: i for i, k in enumerate(['Manual', 'Automatic'])}
seller_mapping = {k: i for i, k in enumerate(['Individual', 'Corporate', 'Commercial Registration'])}
color_mapping = {k: i for i, k in enumerate(['White', 'Silver', 'Blue', 'Black', 'Grey', 'Red', 'Others'])}
location_mapping = {k: i for i, k in enumerate(['Mumbai', 'Delhi', 'Bangalore', 'Hyderabad', 'Chandigarh', 'Lucknow', 'Kolkata', 'Ahmedabad', 'Patna', 'Chennai', 'Jaipur', 'Others'])}

make = make_mapping[make]
fuel_type = fuel_mapping[fuel_type]
owner = owner_mapping[owner]
drivetrain = drive_mapping[drivetrain]
transmission = trans_mapping[transmission]
seller_type = seller_mapping[seller_type]
color = color_mapping[color]
Loc = location_mapping[Loc]

if st.button("Predict Price"):
    input_array = np.array([[make, fuel_type, owner, drivetrain, transmission, seller_type,Loc, color, year, km, fc, sc, engine, power_bhp,power_rpm, torque_nm, torque_rpm, length, width, height]])

    try:
        price = model.predict(input_array)[0]
        st.success(f"Estimated Car Price: ₹ {price:,.2f}")
    except Exception as e:
        st.error("Prediction failed. Please check input values or model compatibility.")
        st.exception(e)
