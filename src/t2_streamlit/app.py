import streamlit as st

page_1 = st.Page("pages/upload.py", title="Upload Picture", icon="🖼️")
page_2 = st.Page("pages/all.py", title="All Data")

pg = st.navigation({
    "upload" : [page_1],
    "chart" : [page_2]
    })
pg.run()
