import streamlit as st
def main():
    pg = st.navigation([
        st.Page('info.py', title="Home", icon=':material/home:'),
        st.Page('prediction.py', title="Predict", icon=':material/stethoscope:'),
    ])
    pg.run()

if __name__ == "__main__":
    main()
st.title("Welcome to Car Price Prediction App")
st.markdown("""
This app helps you **predict the price of a used car** based on various features like make, Engine , year, mileage, and more.

Use the sidebar to navigate between:
- **Home** - You're here!
- **Info** - Learn about the data and features used.
- **Predict** - Enter car details and get the estimated price.
""")
