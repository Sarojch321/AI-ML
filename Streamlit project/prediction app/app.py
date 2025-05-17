import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import predict

st.set_page_config(
  page_title="Diabetes prediction app",
  layout="wide"
)

st.title("Diabetes prediction app")
st.write("""
  This app predicts the likehood of a patient having diabetes based on various health metrics.
""")

# sidebar
st.sidebar.title("Navigation")
options = st.sidebar.radio("select a page:",
                  ["Prediction", "About"])

if options == "Prediction":
  st.header("Patient Information")
  col1, col2, col3 = st.columns(3)

  with col1:
    pregnancy = st.number_input("Pregnancy:",min_value= 0, max_value= 36, value= 0)
    glucose = st.number_input("Glucose:",0,400,0)
    blood_pressuse = st.number_input("Blood pressure:",0,200,120)

  with col2:
    skin_thickness = st.number_input("Skin thickness:",0,100,0)
    insulin = st.number_input("Insulin:",0,200,0)
    bmi = st.number_input("BMI:",10,100,10)

  with col3:
    diabetes_pedigree_function = st.number_input("Diabetes Pedigree Function:",0,1,0)
    age = st.number_input("Age:", 15,99,40)


  if st.button("Predict diabetes risk"):
    input_data = [
      pregnancy, glucose, blood_pressuse, skin_thickness, insulin, bmi, diabetes_pedigree_function, age
    ]

    prediction = predict.predict_diabetes(input_data)

    st.subheader("Prediction result")
    if prediction == 1:
      st.warning("Chance of diebetes")
      st.warning("Please consult to hospital")

    else:
      st.success("Less chance if diabetes")