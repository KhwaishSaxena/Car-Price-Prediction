import streamlit as st
import pandas as pd
import numpy as np
import pickle

#model = pickle.load(open("xgboost_model.pkl", "rb"))
# Get absolute path of current directory (pages/)
current_dir = os.path.dirname(__file__)
model_path = os.path.join(current_dir, "xgboost_model.pkl")

with open(model_path, "rb") as f:
    model = pickle.load(f)
st.title('Car Price Prediction')

make = st.selectbox("Make", ['Honda', 'Maruti Suzuki', 'Hyundai', 'Toyota', 'Mercedes-Benz', 'BMW', 'Skoda', 'Nissan', 'Renault', 'Tata', 'Volkswagen', 'Ford', 'Audi', 'Mahindra', 'MG', 'Jeep', 'Porsche', 'Kia', 'Land Rover', 'Volvo', 'Maserati', 'Jaguar', 'Isuzu', 'Fiat', 'MINI', 'Ferrari', 'Mitsubishi', 'Datsun', 'Lamborghini', 'Chevrolet', 'Ssangyong', 'Rolls-Royce', 'Lexus'], help = "Company Of the car")

fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG", "Others", "Electric"], help = "Fuel type of the car")

owner = st.selectbox("Owner", ['First','Second','3 or More','UnRegistered Car'], help = "Number of previous owners")

drivetrain = st.selectbox("Drivetrain", ['FWD','RWD','AWD'], help = "AWD/RWD/FWD" )

transmission = st.selectbox("Transmission", ['Manual','Automatic'], help = "Gear transmission of the car")

seller_type = st.selectbox("Seller Type ", ['Individual','Corporate','Commercial Registration'], help = "tells if car is sold by individual or dealer")

color = st.selectbox("Color", ['White','Silver','Blue','Black','Grey','Red','Others'], help = "Color of the car")

Loc = st.selectbox("Location", ['Mumbai','Delhi','Bangalore','Hyderabad','Chandigarh','Lucknow','Kolkata','Ahmedabad','Patna','Chennai','Jaipur','Others' ], help = "City in which car is being sold")

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
