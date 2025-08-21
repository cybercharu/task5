import streamlit as st
user=st.text_input("Name")
st.write(f"Hello, {user}!!")
x=st.text_input("Age")
chosen = st.radio(
        'Sex',
        ("Male", "Female"))
slider = st.slider(
    'Select a range of BMI',
    0.0, 100.0, (0.0, 100.0)
)
y=st.text_input("Number of Children")
choose = st.radio(
        'Smoker',
        ("Yes", "No"))
option = st.selectbox(
    'Regions',
     ('southwest','southeast', 'northwest', 'northeast'))

st.write(f"User age is : {x}")
st.write(f"User is : {chosen}")
st.write(f"User BMI is : {slider}")
st.write(f"User has how many Children : {y}")
st.write(f"User smokes : {choose}")
st.write(f"User selected : {option}")
