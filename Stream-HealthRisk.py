import pickle
import streamlit as st

health_model = pickle.load(open('HealthRisk-model.sav', 'rb'))

st.title('Prediction Health Risk')

Age = st.number_input ('Input Nilai Age')
SystolicBP = st.number_input ('Input Nilai SystolicBP')
DiastolicBP = st.number_input ('Input Nilai DiastolicBP')
BS = st.number_input ('Input Nilai BS')
BodyTemp = st.number_input ('Input Nilai BodyTemp')
HeartRate = st.number_input ('Input Nilai HeartRate')

health_diagnosis = ''

if st.button('Test Prediction') :
    health_prediction = health_model.predict([[Age, SystolicBP, DiastolicBP, BS, BodyTemp, HeartRate]])

    if (health_prediction[0] == 0):
        health_diagnosis = 'Low Risk'
    else :
        health_diagnosis = 'High Risk'
    
st.success(health_diagnosis)