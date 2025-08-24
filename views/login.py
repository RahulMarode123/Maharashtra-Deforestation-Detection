import streamlit as st
import pandas as pd
import os

USERS_FILE = "data/users.csv"

def load_users():
    if os.path.exists(USERS_FILE):
        return pd.read_csv(USERS_FILE)
    return pd.DataFrame(columns=["username", "password"])

def show_login():
    st.subheader("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        users = load_users()
        if ((users['username'] == username) & (users['password'] == password)).any():
            st.success(f"Welcome back, {username}!")
            st.session_state["logged_in"] = True
        else:
            st.error("Invalid credentials. Please try again.")
