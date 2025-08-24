import streamlit as st
import pandas as pd
import os

USERS_FILE = "data/users.csv"

# --- Function to load users ---
def load_users():
    if os.path.exists(USERS_FILE):
        return pd.read_csv(USERS_FILE)
    else:
        return pd.DataFrame(columns=["username", "password"])

# --- Function to save new user ---
def save_user(username, password):
    users = load_users()
    if username in users['username'].values:
        return False  # username already exists
    new_user = pd.DataFrame([[username, password]], columns=["username", "password"])
    users = pd.concat([users, new_user], ignore_index=True)
    users.to_csv(USERS_FILE, index=False)
    return True

# --- Streamlit UI ---
st.title("🌳 Maharashtra Deforestation Detection - Login Page")

menu = ["Login", "Register"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Login":
    st.subheader("Login Section")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        users = load_users()
        if ((users['username'] == username) & (users['password'] == password)).any():
            st.success(f"Welcome {username} 👋")
            st.session_state["logged_in"] = True
        else:
            st.error("Invalid Username or Password ❌")

elif choice == "Register":
    st.subheader("Create New Account")

    new_user = st.text_input("New Username")
    new_pass = st.text_input("New Password", type="password")

    if st.button("Register"):
        if save_user(new_user, new_pass):
            st.success("✅ Account created successfully! Now go to Login")
        else:
            st.warning("⚠️ Username already exists")
