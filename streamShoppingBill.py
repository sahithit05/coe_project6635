import streamlit as st
st.title("Shopping bills")
sal=st.number_input("Enter your Salary")
bill1=st.number_input("enter your first bill")
bill2=st.number_input("enter your second bill")
bill3=st.number_input("enter your third bill")
total=bill1+bill2+bill3
if st.button("Total Bill"):
    st.success(total)
if st.button("percentage"):
    perc=(total/sal)*100
    st.success(perc)