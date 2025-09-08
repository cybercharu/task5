import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

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
    price = predict_price(user_input)
    st.success(f"{user} your Predicted Insurance Cost: ₹{price}")

if st.button("Show Model Performance"):
    score, y_test, y_pred = train_model()
    st.write(f"Model R² Score: {score:.2f}")
    fig, ax = plt.subplots()
    ax.plot(y_test, label="Actual", color="green", marker="o")
    ax.plot(y_pred, label="Predicted", color="orange", marker="x")
    ax.set_xlabel("Sample Index")
    ax.set_ylabel("Charges")
    ax.set_title("Actual vs Predicted")
    ax.legend()
    st.pyplot(fig)

    