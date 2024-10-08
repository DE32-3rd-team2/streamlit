import streamlit as st

page_1 = st.Page("pages/upload.py", title="Upload Picture", icon="🖼️")
page_2 = st.Page("pages/all.py", title="All")
page_3 = st.Page("pages/label.py", title="Add label")

pg = st.navigation({
    "Upload" : [page_1],
    "Data" : [page_2, page_3]
    })
pg.run()
