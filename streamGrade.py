import streamlit as st
st.title("Student Grade")
project=st.number_input("Enter your project marks",min_value=1,step=1)
internal=st.number_input("Enter your internal marks",min_value=1,step=1)
external=st.number_input("Enter your external marks",min_value=1,step=1)
if st.button("grade"):
    if project>=50 and internal>=50 and external>=50:
        pro=(70/100)*project
        inte=(10/100)*internal
        exe=(20/100)*external
        total=pro+exe+inte
        if total>90 :
            st.success("A grade")
        elif total>=80 :
            st.success("B grade")
        else:
            st.success("C grade")
    else:
        if project<50:
            st.success(f"failed in project with {project}")
        if internal < 50:
            st.success(f"failed in internal with {internal}")
        if external < 50:
            st.success(f"failed in external with {external}")