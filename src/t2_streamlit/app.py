import streamlit as st

page_1 = st.Page("pages/upload_pic.py", title="Upload Picture", icon="🖼️")

pg = st.navigation([page_1])
pg.run()
