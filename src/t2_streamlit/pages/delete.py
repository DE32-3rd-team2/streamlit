import streamlit as st
import pandas as pd
import numpy as np
import requests
import os

st.title("All Data")

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

ip = os.getenv("EC2_IP", "localhost")

def load_data():
    url = f"http://{ip}:8022/all"
    r = requests.get(url).json()
    return r

data = load_data()
df = pd.DataFrame(data)

for i in range(len(df)):
    with st.container(border=True):
        img, info = st.columns([1, 3])
        img.image(df['file_path'][i], width=100)
        info.markdown(f"#### {df['num'][i]}. {df['origin_name'][i]}")
        with info.container():
            l, r = st.columns([3, 1])
            l.markdown(f"**예측 결과** : {age_mapping[int(df['prediction_result'][i])]}")
            l.markdown(f"**실제 정답** : {age_mapping[int(df['answer'][i])]}")
            if r.button("Delete", key=i, type="primary"):
                url = f"http://{ip}:8022/delete?num={df['num'][i]}"
                r = requests.get(url)
                st.rerun()

