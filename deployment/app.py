import streamlit as st
import eda
import prediction

# Set Config dan icon
st.set_page_config(
        page_title='Churn Prediction',
        layout='wide',
        )

# Hide Streamlit Style
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

# Membuat navigasi
navigation = st.sidebar.selectbox('Pilih Halaman (Tweet Prediction/EDA): ', ('Tweet Prediction','Exploratory Data Analysis'))

# Run modul dengan if else
if navigation == 'Tweet Prediction' :
    prediction.run()
else :
    eda.run()