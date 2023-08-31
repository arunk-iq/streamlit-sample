import streamlit as st
st.write("Input 3 numbers in below fields")
number1 = st.number_input("First number")
number2 = st.number_input("Second number")
number3 = st.number_input("Third number")
if st.button('Get Max Number'):
    st.write(max(number1,number2,number3))

