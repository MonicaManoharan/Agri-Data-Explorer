import streamlit as st
import pandas as pd
from Login import login
from FarmerModule import farmer_dashboard
from PolicyModule import policymaker_dashboard
from ResearchModule import researcher_dashboard

st.set_page_config(layout="wide", page_title="AgriData Explorer")

def main():
    df = pd.read_csv("Cleaned_ICRISAT_Data.csv")

    if "logged_in" not in st.session_state:
        login()
    else:
        role = st.session_state["role"]
        # set_role_background(role)

        # st.sidebar.image("assets/sidebar_image.png", use_container_width=True)
        st.sidebar.header(f"Logged in as: {role}")
        if st.sidebar.button("Logout"):
            st.session_state.clear()
            st.rerun()

        if role == "Farmer":
            farmer_dashboard(df)
        elif role == "Policymaker":
            policymaker_dashboard(df)
        elif role == "Researcher":
            researcher_dashboard(df)


if __name__ == "__main__":
    main()
