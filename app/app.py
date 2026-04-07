import streamlit as st

st.title("Simple Reactive App")

# Text input
user_input = st.text_input("Type something:")

# Reactive output
if user_input:
    st.write(f"You typed: {user_input}")
else:
    st.write("Start typing above 👆")