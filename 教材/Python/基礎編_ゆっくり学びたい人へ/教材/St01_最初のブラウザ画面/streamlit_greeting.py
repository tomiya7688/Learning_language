# streamlitを、このプログラムで st という名前で使えるようにする
import streamlit as st

# ブラウザ画面に「名前を入力してみよう」というタイトルを表示する
st.title("名前を入力してみよう")

# 「名前」と表示した入力欄をブラウザ画面に置き、入力された文字列を name に入れる
name = st.text_input("名前")

# name が空の文字列でなければ、次の処理を実行する
if name:
    # ブラウザ画面に「こんにちは」と name の値を表示する
    st.write("こんにちは", name)
