import streamlit as st
import pandas as pd

def show_login():
    st.subheader("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        try:
            users = pd.read_csv("users.csv")
            if ((users["username"] == username) & (users["password"] == password)).any():
                st.success("Logged in successfully!")
                st.session_state["logged_in"] = True
            else:
                st.error("Invalid username or password")
        except FileNotFoundError:
            st.error("No registered users found. Please register first.")
