import streamlit as st
import functions

st.title("To do")

todos = functions.get_todos()

for todo in todos:
    st.checkbox(todo)


st.text_input(label="", placeholder="Enter a todo")