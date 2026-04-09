import streamlit as st
import pandas as pd
from io import StringIO

st.set_page_config(page_title="Trakingo", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    .stButton>button { width: 100%; background-color: #007bff; color: white; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

st.title("📦 TRΛKINGO")

access_key = st.sidebar.text_input("Access Key", type="password")

if access_key == "admin123":
    st.header("Admin Dashboard")
    client_id = st.text_input("Assign to Client ID (e.g., Client01)")
    data_input = st.text_area("Paste Excel Rows Here", height=200)
    
    # Large button for mobile tapping
    if st.button("GENERATE TRACKER"):
        if data_input:
            df = pd.read_csv(StringIO(data_input), sep='\t')
            st.success(f"Tracking Loaded for {client_id}")
            st.dataframe(df, use_container_width=True)
        else:
            st.error("Please paste your Excel data first.")

elif access_key:
    st.header(f"Portal: {access_key}")
    st.info("Searching for your specific procurement lines...")
    # This is where your logic to show specific client data will go next
else:
    st.warning("Please enter your Access Key in the sidebar.")
