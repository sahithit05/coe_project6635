import streamlit as st
st.title("Gross salary")
basic_sal=st.number_input("Enter your salary",min_value=1,step=1)
hra=0
da=0
if st.button("Gross salary"):
    if basic_sal<10000 :
        hra=(67/100)*basic_sal
        da=(73/100)*basic_sal
    elif basic_sal < 20000:
        hra = (69 / 100) * basic_sal
        da = (76 / 100) * basic_sal
    else:
        hra = (73 / 100) * basic_sal
        da = (89 / 100) * basic_sal
gs = hra + da + basic_sal
st.success(gs)