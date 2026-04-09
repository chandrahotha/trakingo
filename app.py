import streamlit as st
import pandas as pd
from io import StringIO

st.set_page_config(page_title="Trakingo", layout="wide")

# Premium Dark Theme CSS
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    .stDataFrame { border: 1px solid #30363d; border-radius: 10px; }
    </style>
""", unsafe_allow_html=True)

st.title("📦 TRΛKINGO")

# Admin Key for you, Client Name for them
access_key = st.sidebar.text_input("Access Key", type="password")

if access_key == "admin123":
    st.header("Admin Dashboard")
    data_input = st.text_area("Paste Excel Rows Here")
    if st.button("Display Data"):
        df = pd.read_csv(StringIO(data_input), sep='\t')
        st.dataframe(df, use_container_width=True)
elif access_key:
    st.header(f"Client Portal: {access_key}")
    st.info("Tracking data will appear here.")
else:
    st.warning("Please enter your Access Key to begin.")
