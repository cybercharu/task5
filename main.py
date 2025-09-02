import streamlit as st
import pandas as pd
import os
import seaborn as sns
import numpy as np 
import matplotlib.pyplot as plt

from predict import train_model,predict_price

st.title("Predict Medical Insurance Cost")

user=st.text_input("Name")
st.write(f"Hello, {user}!!")
age = st.number_input("Age", min_value=0, max_value=120, step=1, value=25)
bmi = st.number_input("BMI", min_value=0.0, max_value=100.0, step=0.1, value=25.0)
children = st.number_input("Number of Children", min_value=0, max_value=10, step=1, value=0)
sex = st.radio("Sex", ("male", "female"))
smoker = st.radio("Smoker", ("yes", "no"))
region = st.selectbox("Regions", ('southwest','southeast','northwest','northeast'))

user_input = {
        "age": age,
        "sex": sex,
        "bmi": bmi,
        "children": children,
        "smoker": smoker,
        "region": region
      }
if st.button("Predict Charges"):
    #score = train_model()
    #st.success(f"Model Score: {score}")
    price = predict_price(user_input)
    st.success(f"{user} your Predicted Insurance Cost: ₹{price}")

st.subheader("Predicted Insurance Cost")

price = predict_price(user_input)

df_price = pd.DataFrame({
    "Category": ["Predicted Price"],
    "Value": [price]
})
fig, ax = plt.subplots()
sns.barplot(data=df_price, x="Category", y="Value", ax=ax, color="green")
for patch in ax.patches:
    current_width = patch.get_width()
    patch.set_width(current_width * 0.3)  
    patch.set_x(patch.get_x() + current_width * 0.35)  
ax.set_ylabel("Insurance Charges (₹)")
ax.set_title("Predicted Insurance Cost")
st.pyplot(fig)


