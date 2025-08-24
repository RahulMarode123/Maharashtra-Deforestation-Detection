import streamlit as st
import pandas as pd
import os

USERS_FILE = "data/users.csv"

# Load users from CSV
def load_users():
    if os.path.exists(USERS_FILE):
        return pd.read_csv(USERS_FILE)
    else:
        return pd.DataFrame(columns=["username", "password"])

# Save users to CSV
def save_user(username, password):
    df = load_users()
    if username in df["username"].values:
        return False  # already exists
    new_user = pd.DataFrame([[username, password]], columns=["username", "password"])
    df = pd.concat([df, new_user], ignore_index=True)
    df.to_csv(USERS_FILE, index=False)
    return True

def login_page():
    st.title("🔐 Login Page")

    menu = ["Login", "Register"]
    choice = st.radio("Choose Option", menu)

    if choice == "Login":
        username = st.text_input("Enter Username:")
        password = st.text_input("Enter Password:", type="password")

        if st.button("Login"):
            df = load_users()
            if username in df["username"].values and password in df["password"].values:
                st.success(f"Welcome {username}!")
                st.session_state["logged_in"] = True
            else:
                st.error("Invalid Username or Password")

    elif choice == "Register":
        st.subheader("Create New Account")
        new_username = st.text_input("New Username:")
        new_password = st.text_input("New Password:", type="password")

        if st.button("Register"):
            if save_user(new_username, new_password):
                st.success("✅ Account created successfully! Please login.")
            else:
                st.error("⚠️ Username already exists!")
