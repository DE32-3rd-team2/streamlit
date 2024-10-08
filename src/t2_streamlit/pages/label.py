import streamlit as st
import pandas as pd
import numpy as np
import requests
import os

age_mapping = {
        '0-2 years': 0,
        '3-9 years': 1,
        '10-19 years': 2,
        '20-29 years': 3,
        '30-39 years': 4,
        '40-49 years': 5,
        '50-59 years': 6,
        '60-69 years': 7,
        '70+ years': 8
}

ip = os.getenv("EC2_IP", "localhost")

def load_data():
    url = f"http://{ip}:8022/one"
    r = requests.get(url).json()
    return r

data = load_data()

if data:
    data = data[0]
    with st.container(border=True):
        img, info = st.columns([1, 3])
        img.image(data['file_path'], width=100)

        with info.container():  
            st.markdown(f"#### {data['num']}") #. {data['origin_name']}")
            st.markdown(f"**예측 결과** ➡️ {data['prediction_result']}")

            label = st.selectbox("**실제 정답**", options=age_mapping.keys())

            if st.button("Update"):
                url = f"http://{ip}:8022/up?num={data['num']}&label={age_mapping[label]}"
                r = requests.get(url)

                if r.status_code==200:
                    st.rerun()
