import streamlit as st
import pandas as pd
import numpy as np
import requests
import os

def load_data():
    ip = os.getenv("EC2_IP", "localhost")
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
        info.write(f"예측 결과 : {df['prediction_result'][i]}")
        info.write(f"실제 정답 : {df['answer'][i]}")
