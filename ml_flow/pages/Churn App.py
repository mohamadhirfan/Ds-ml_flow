import streamlit as st
import numpy as np
import sklearn
import pandas as pd
import os
from pickle import load
from matplotlib import image

st.set_page_config(page_title="Churn Prediction App In Telecommunication",
                   layout="centered")

st.sidebar.subheader(":green[Churn Prediction App In Telecommunication:]")
st.sidebar.markdown(":blue[Here you can enter you values and check wheater the customer Churn or not:]")

st.markdown("""
    <style>
        body {
            background-image: url("https://tse1.mm.bing.net/th?id=OIP.aJc5ai_dUw8QmiT82NBX_gHaEo&pid=Api&P=0");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
        .stApp {
            background-color: rgba(255, 255, 255, 0.1);
        }
    </style>
""", unsafe_allow_html=True)

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
dir_of_interest = os.path.join(PARENT_DIR, "resources")

sc = os.path.join(dir_of_interest,'standard_scaler.pkl')
ohe = os.path.join(dir_of_interest,'OneHot_Encoder.pkl')
lr = os.path.join(dir_of_interest,'lr_model.pkl')

scaler=load(open(sc,'rb'))
ohec = load(open(ohe, 'rb'))
lr_model = load(open(lr, 'rb'))

st.markdown("<h2 style='color: white;'>Churn Testing:</h2>", unsafe_allow_html=True)

tenure = st.number_input('tenure')
PhoneService=st.selectbox('PhoneService',['Yes','No'])
InternetServipwce=st.selectbox('InternetServipwce',['Fiber optic','DSL','No'])
Contract=st.selectbox('Contract',['Month','Two year','One year'])
PaymentMethod=st.selectbox('PaymentMethod',['Electronic check','Mailed check','Bank transfer (automatic)','Credit card (automatic)'])
MonthlyCharges= st.number_input('MonthlyCharges')
TotalCharges= st.number_input('TotalCharges')

btn_click=st.button("predict")
if btn_click:
    if tenure and PhoneService and InternetServipwce and Contract and PaymentMethod and MonthlyCharges and TotalCharges:
        num = np.array([float(tenure),float(MonthlyCharges),float(TotalCharges)]).reshape(1,-1)
        num_rescaled=scaler.transform(num)
        cat = np.array([str(PhoneService),str(InternetServipwce),str(Contract),str(PaymentMethod)]).reshape(1,-1)
        cat_trans = ohec.transform(cat)
        query_point_trans=np.concatenate([num_rescaled,cat_trans],axis=1)
        pred=lr_model.predict(query_point_trans)
        st.text(' predict if the customer will churn or not.')
        st.success(pred,icon="✅")
    else:
        st.error("enter the values properly",icon="🚨")