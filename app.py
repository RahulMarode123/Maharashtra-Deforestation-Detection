import streamlit as st
import login
import register
import main

# ✅ Initialize session state first
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

st.title("Maharashtra Deforestation Detection App")

menu = ["Login", "Register", "Main"]
choice = st.sidebar.selectbox("Navigation", menu)

if choice == "Login":
    login.show_login()

elif choice == "Register":
    register.show_register()

elif choice == "Main":
    if st.session_state.get("logged_in"):
        main.show_main()
    else:
        st.warning("Please login first!")
