import streamlit as st
#streamlit run calculator.py
st.title("Calculator")
st.markdown("Welcome to my page")

c1,c2 = st.columns(2)
fnum=c1.number_input("Enter fist number",value=1)
snum=c2.number_input("Enter second number",value=0)
 

options=['Add','Subtract','Multiply','Divide']
choice=st.radio('Select Operations',options)
button=st.button("calculate")
result=0
if button:
    if choice=='Add':
        result=fnum+snum
    if choice=='Subtract':
        result=fnum-snum
    if choice=='Multiply':
        result=fnum*snum
    if choice=='Divide':
        result=fnum/snum

st.success(f"The result is {result}")