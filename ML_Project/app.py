import streamlit as st
st.tittle("My First Strealit App")
name=st.text_inout("Enter Your Name")
if name:
    st.write("Hello",name)
