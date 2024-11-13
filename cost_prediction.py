import streamlit as st
import pandas as pd
import pickle

data = pd.read_excel("C:/Users/Arasu/OneDrive/Documents/GitHub/Project/insurance_cost_prediction.xlsx")

st.write(
   """
   # Insurance Cost Prediction
   """  
)

st.dataframe(data.head())

col1,col2 = st.columns(2)

Diabetes = col1.selectbox("Select whether you have diabetes or not (0- indicates 'No' and 1 -indicates 'Yes')",
                        [0,1])

BloodPressureProblems = col2.selectbox("Select whether you have Blood Pressure or not (0- indicates 'No' and 1 -indicates 'Yes')",
                        [0,1])

AnyTransplants = col1.selectbox("Select whether you have done any transplants or not (0- indicates 'No' and 1 -indicates 'Yes')",
                        [0,1])

AnyChronicDiseases = col2.selectbox("Select whether you have chronic disease or not (0- indicates 'No' and 1 -indicates 'Yes')",
                        [0,1])

KnownAllergies = col1.selectbox("Select whether you have Allergies or not (0- indicates 'No' and 1 -indicates 'Yes')",
                        [0,1])

HistoryOfCancerInFamily = col2.selectbox("Select whether anyone in your family had cancer or not (0- indicates 'No' and 1 -indicates 'Yes')",
                        [0,1])

NumberOfMajorSurgeries = col1.selectbox("Select how many surgeries you had in past (0- indicates 'No Surgery', 1 -indicates 'One Surgery' and 2 -indicates 'Two Surgery')",
                        [0,1,2])

Age = col2.number_input("Enter your age", step=1, format="%d")

Height = col1.number_input("Enter your height", step=1, format = "%d")

Weight = col2.number_input("Enter your weight", step=1, format = "%d")

def model_pred(Diabetes,BloodPressureProblems,AnyTransplants,AnyChronicDiseases,HistoryOfCancerInFamily,NumberOfMajorSurgeries,Age):
    with open("cost_prediction_pickle", "rb") as file:
        rf_model = pickle.load(file)
    input_features = [[Diabetes,BloodPressureProblems,AnyTransplants,AnyChronicDiseases,HistoryOfCancerInFamily,NumberOfMajorSurgeries,Age]]
    return rf_model.predict(input_features)

if (st.button("Predict cost")):
    cost = model_pred(Diabetes,BloodPressureProblems,AnyTransplants,AnyChronicDiseases,HistoryOfCancerInFamily,NumberOfMajorSurgeries,Age)
    st.text(f"The insurance cost is {cost[0].round(2)} rupees.")
