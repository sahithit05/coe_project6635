import streamlit as st
num1=st.number_input("Enter number1",min_value=1,step=1)
num2=st.number_input("Enter number2",min_value=1,step=1)
if st.button("Addition"):
    st.success(num1+num2)
if st.button("subtraction"):
    st.success(num1-num2)
if st.button("multiplication"):
    st.success(num1*num2)
if st.button("division"):
    st.success(num1/num2)