import streamlit as st
import random

st.set_page_config(layout="wide")
st.title('Test Streamlit')
st.write('Lose Media Society')

result1 = st.button("click me!")
if result1 :
    st.write("you click 1")

result2 = st.button("click me!!", type="tertiary")
if result1 & result2:
    st.write("you click both")

st.button("reset", type="primary")

if st.button('Generate Random Number'):
    random_number = random.randint(1, 100)
    st.write(f'Random Number: {random_number}')