import streamlit as st
from components.navbar import navbar

def show_Datasets():
    navbar("Datasets")
    st.title("Datasets")

    # --- Sub Page 1 ---
    col1, col2 = st.columns([1,2])
    with col1:
        if st.button("➡ Go to Sub Page 1"):
            st.session_state.page = "Amravati"
            st.rerun()
    with col2:
        st.image(
            r"C:\Users\parvi\OneDrive\Documents\streamlit-deforest\Multipage\images\mah1.webp",
            caption="Primary Forest Loss in Maharashtra"
        )

    st.markdown("---")  # Divider line

    # --- Sub Page 2 ---
    col3, col4 = st.columns([1,2])
    with col3:
        if st.button("➡ Go to Sub Page 2"):
            st.session_state.page = "page1_sub2"
            st.rerun()
    with col4:
        st.image(
            r"C:\Users\parvi\OneDrive\Documents\streamlit-deforest\Multipage\images\mah1.webp",
            caption="Another Example"
        )

    st.markdown("---")

    # --- Sub page 3 ---
    col5, col6 = st.columns([1,2])
    with col5:
        if st.button("⬅ Datsets"):
            st.session_state.page = "main"
            st.rerun()
    with col6:
        st.image(
            r"C:\Users\parvi\OneDrive\Documents\streamlit-deforest\Multipage\images\mah1.webp",
            caption="Go Back"
        )
