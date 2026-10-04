import streamlit as st

st.title("名前を入力してみよう")

name = st.text_input("名前")

if name:
    st.write("こんにちは", name)
