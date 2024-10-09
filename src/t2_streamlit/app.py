import streamlit as st

page_u1 = st.Page("pages/upload.py", title="Upload Image", icon="🖼️")
page_u2 = st.Page("pages/all.py", title="Result", icon="👓")
page_c1 = st.Page("pages/age_acc.py", title="Age Group")
page_M1 = st.Page("pages/admin.py", title="관리자 페이지", icon="⚙️")

pg = st.navigation({
    "User" : [page_u1, page_u2],
    "Chart" : [page_c1],
    "Manage" : [page_M1],
    })

pg.run()
