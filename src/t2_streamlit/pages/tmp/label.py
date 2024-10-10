import streamlit as st
import pandas as pd
import numpy as np
import requests
import os

st.title("관리자 모드")

age_mapping = {
    0: '0-2 years',
    1: '3-9 years',
    2: '10-19 years',
    3: '20-29 years',
    4: '30-39 years',
    5: '40-49 years',
    6: '50-59 years',
    7: '60-69 years',
    8: '70+ years'
}

reversed_age_mapping = {v: k for k, v in age_mapping.items()}

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
            st.markdown(f"**예측 결과** ➡️ {age_mapping[int(data['prediction_result'])]}")

            label = st.selectbox("**실제 정답**", options=age_mapping.values())

            if st.button("Update"):
                url = f"http://{ip}:8022/up?num={data['num']}&label={reversed_age_mapping[label]}"
                r = requests.get(url)

                if r.status_code==200:
                    st.rerun()
else:
    st.warning("데이터가 없습니다.")
