import streamlit as st

def app():
    st.title("Subtraction of two numbers")
    a = st.number_input("Enter first number")
    b = st.number_input("Enter second number")
    c = a - b
    st.write("Subtraction of two numbers is", c)

if __name__ == "__main__":
    app()