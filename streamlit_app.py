import streamlit as st
st.write("Input 3 numbers in below fields")
number1 = st.number_input("First number", format='%d')
number2 = st.number_input("Second number", format='%d')
number3 = st.number_input("Third number", format='%d')
if st.button('Get Max Number'):
    st.write("Maximum Number:',max(number1,number2,number3))

