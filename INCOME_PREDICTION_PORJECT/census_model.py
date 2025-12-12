import pandas as pd
import streamlit as st
import pickle

#load model
#with open (r"C:\data science_20\data science__20\Machine learning\census_model.pkl", "rb") as file:
    #model = pickle.load(file)
import pickle

with open("census_model.pkl", "rb") as file:
    model = pickle.load(file)


st.title("Income Prediction webapp")
st.write("predict whether person income is >50k or <50k")

def user_input():
     age = st.number_input("Age", 17, 90)
     workclass = st.selectbox("workclass", ["priver", "Goverment", "Self_Employed", "Without_pay"])
     fnlwgt = st.number_input("Fnlwgt", 10000, 1500000)
     education = st.selectbox(
          "Education",
          ["HighSchool", "HighSecoundry", "Bechelors", "Master", "Doctorate", "Middle", "Primary"]
     )
     education_num = st.number_input("Education_Num", 1, 16)

     marital_status = st.selectbox(
          "Marital Status",
          ['single', 'couple']
     )

     occupation = st.selectbox(
          "occupation",
          [
               'Adm-clerical', 'Exec-managerial', 'Handlers-cleaners',
               'Prof-specialty', 'Other-service', 'Sales', 'Craft-repair',
               'Transport-moving', 'Farming-fishing', 'Machine-op-inspct',
               'Tech-support', 'Protective-serv', 'Armed-Forces',
               'Priv-house-serv'
          ]
     )

     relationship = st.selectbox("relationship",
          ['Not-in-family', 'Husband', 'Wife', 'Own-child', 'Unmarried', 'Other-relative']
     )

     race = st.selectbox("race",
          ['White', 'Black', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo', 'Other']
     )

     sex = st.selectbox("sex", ['Male','Female'])
     capital_gain = st.number_input("capital-gain", 0)
     capital_loss = st.number_input("capital-loss", 0, 4400)
     hours_per_week = st.selectbox("hours-per-week", list(range(1, 101)))
     native_country = st.selectbox("native-country", ["US","Others"])

     # FIXED VERSION (all values inside list)
     data = {
          'age': [age],
          'workclass': [workclass],
          'fnlwgt': [fnlwgt],
          'education': [education],
          'education-num': [education_num],
          'marital-status': [marital_status],
          'occupation': [occupation],
          'relationship': [relationship],
          'race': [race],
          'sex': [sex],
          'capital-gain': [capital_gain],
          'capital-loss': [capital_loss],
          'hours-per-week': [hours_per_week],
          'native-country': [native_country]
     }

     return pd.DataFrame(data)

    
input_df = user_input()

st.subheader("UserInputData")
st.write(input_df)



if st.button("Predict Income"):
     prediction = model.predict(input_df)[0]
     if prediction == ">50k":
          st.success("Prediction Income:- >50k")
     else:
          st.success("Prediction Income :- <50k")