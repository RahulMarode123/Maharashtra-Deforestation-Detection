import streamlit as st
import pandas as pd
import os

USERS_FILE = "data/users.csv"

def load_users():
    if os.path.exists(USERS_FILE):
        return pd.read_csv(USERS_FILE)
    return pd.DataFrame(columns=["username", "password"])

def save_user(username, password):
    users = load_users()
    if username in users["username"].values:
        return False
    users = pd.concat([users, pd.DataFrame([[username, password]], columns=["username", "password"])], ignore_index=True)
    users.to_csv(USERS_FILE, index=False)
    return True

def show_register():
    st.subheader("Register")

    new_user = st.text_input("New Username")
    new_pass = st.text_input("New Password", type="password")

    if st.button("Register"):
        if save_user(new_user, new_pass):
            st.success("Account created! Please click Login to proceed.")
        else:
            st.error("Username already exists. Choose a different name.")
