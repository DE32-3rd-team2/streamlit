import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import requests
import os

age_band_mapping = {
    0: '0-2',
    1: '3-9',
    2: '10-19',
    3: '20-29',
    4: '30-39',
    5: '40-49',
    6: '50-59',
    7: '60-69',
    8: '70+'
}

st.title("나이대 별 예측 정확도")

def load_data():
    ip = os.getenv("EC2_IP", "localhost")
    url = f"http://{ip}:8022/agg"

    r = requests.get(url).json()
    return r

data = load_data()
df = pd.DataFrame(data)

df['accuracy'] = df['correct'] / df['total_count']
df['age_band'] = df['answer'].map(age_band_mapping)
df = df.sort_values(by="answer")

fig, ax = plt.subplots(figsize=(10, 6))

sns.barplot(x="age_band", y="accuracy", data=df, ax=ax)

ax.set_title("Prediction Accuracy by Age band")
ax.set_xlabel("Age Band")
ax.set_ylabel("Accuracy")

st.pyplot(fig)
