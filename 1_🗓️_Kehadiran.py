import pandas as pd
import base64
import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.set_page_config(
    page_title="Web Absensi",
    page_icon="📆"
)

@st.cache_data
def get_img_as_base64(file):
    with open(file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_img_as_base64("foto/SAKASMA.jpg")

bg_web = f"""
<style>
[data-testid="stAppViewContainer"]{{
background-image: url("data:image/png;base64,{img}");
background-size: cover;
}}

[data-testid="stHeader"]{{
background-color: rgba(0, 0, 0, 0);
}}

[data-testid="collapseControl"]{{
left: 1rem;
}}

</style>
"""
st.markdown(bg_web, unsafe_allow_html=True)
url = "https://docs.google.com/spreadsheets/d/1OxwoDBP6eDowycuYtNP5_vyvM_j8QBmfu78o_Y8g6XI/edit?usp=sharing"
conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read(spreadsheet=url, usecols=[0, 1, 2])

col1, col2 = st.coolumns(2)
with col1:
    st.dataframe(df)
with col2:
    st.header("Filter Kelas:")

    kelas = st.multiselect(
        "Pilih Kelas:",
        options=df["KELAS"].dropna().unique()
        default=df["KELAS"].dropna().unique()
    )
    df_selection = df.query(
        "KELAS == @kelas"
    )
    st.dataframe(df_selection)
