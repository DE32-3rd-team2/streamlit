import streamlit as st

page_1 = st.Page("pages/upload.py", title="Upload Picture", icon="🖼️")
page_2 = st.Page("pages/camera.py", title="Take a photo", icon="📸")
pg = st.navigation([page_1, page_2])
pg.run()
