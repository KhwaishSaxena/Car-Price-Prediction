import streamlit as st

def main():
    pg = st.navigation([
        st.Page('info.py', title="Home"),
        st.Page('prediction.py', title="Predict"),
    ])
    pg.run()

if __name__ == "__main__":
    main()
