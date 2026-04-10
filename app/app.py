import streamlit as st
import pandas as pd

st.title("Simple Reactive App")

# Text input
user_input = st.text_input("Type something:")

# Reactive output
if user_input:
    st.write(f"You typed: {user_input}")
else:
    st.write("Start typing above 👆")

st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))