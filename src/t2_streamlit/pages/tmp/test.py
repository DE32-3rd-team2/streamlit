import streamlit as st

# 올바른 비밀번호를 설정
CORRECT_PASSWORD = "admin123"

# 세션 상태를 통해 로그인 여부 관리
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

def login():
    """로그인 처리 함수"""
    password = st.text_input("비밀번호를 입력하세요", type="password")
    if st.button("로그인"):
        if password == CORRECT_PASSWORD:
            st.session_state.logged_in = True
            st.success("로그인 성공!")
            st.rerun()
        else:
            st.error("비밀번호가 잘못되었습니다.")

def admin_page():
    """관리 페이지 함수"""
    st.title("관리 페이지")
    st.write("여기에 관리 페이지 내용을 추가하세요.")

# 로그인 여부에 따라 화면을 제어
if not st.session_state.logged_in:
    st.title("관리 페이지 접근")
    login()
else:
    admin_page()

