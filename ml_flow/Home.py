import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image, ImageEnhance
import os
from matplotlib import image


path1=os.getcwd()

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
dir_of_interest1 = os.path.join(FILE_DIR,"resources","images","irfan.png")
st.set_page_config(layout="wide")
st.subheader(":red[About me : :sunglasses: ]")
col1,col2,col3=st.columns(3, gap='small')
with col1:
    st.subheader("[:red[LinkedIn:]](https://www.linkedin.com/in/mohamadhirfan/)")
with col2:
    st.subheader("[:red[GitHub:]](https://github.com/mohamadhirfan?tab=repositories)")
with col3:
    if st.button('Bio'):
        img = image.imread(dir_of_interest1)
        st.subheader(':red[Name: MOHAMADH IRFAN:heart_eyes:]')
        st.subheader(':red[Education: M.Sc-Statistics]')
        st.image(img)
        st.subheader(':red[cool data scientist :sunglasses:]')
st.markdown("""
    <style>
        body {
            background-image: url("https://tse3.mm.bing.net/th?id=OIP.1Wd11So0xosR8h5LQNwhigHaEo&pid=Api&P=0");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
        .stApp {
            background-color: rgba(255, 255, 255, 0.1);
        }
    </style>
""", unsafe_allow_html=True)
            


st.markdown("<h2 style='color: white;'>The data set includes information about:</h2>",unsafe_allow_html=True)
st.markdown('''
    <h6 style='color: black;'>
        1.Customers who left within the last month – the column is called Churn
        <br><br>
        2.Services that each customer has signed up for – phone, multiple lines, internet, online security, online backup, device protection, tech support, and streaming TV and movies
        <br><br>
        3.Customer account information – how long they’ve been a customer, contract, payment method, paperless billing, monthly charges, and total charges
        <br><br>
        4.Demographic info about customers – gender, age range, and if they have partners and dependents
    </h6>
''', unsafe_allow_html=True)

st.markdown("<h2 style='color: white;'>Business Understanding</h2>",unsafe_allow_html=True)
st.markdown('''
    <h6 style='color: black;'>
        The telecommunications sector has become one of the main industries in developed countries. The technical progress and the increasing number of operators raised the level of competition. Companies are working hard to survive in this competitive market depending on multiple strategies. Three main strategies have been proposed to generate more revenues:
            <br><br>
            1.Acquire new customers
            <br><br>
            2.Upsell the existing customers
            <br><br>
            3.Increase the retention period of customers However, comparing these strategies taking the value of return on investment (RoI) of each into account has shown that the third strategy is the most profitable strategy, proving that retaining an existing customer costs much lower than acquiring a new one, in addition to being considered much easier than the upselling strategy. To apply the third strategy, companies have to decrease the potential of customer’s churn, known as "the customer movement from one provider to another".
            <br><br>
            4.Customer Churn is one of the most important and challenging problems for businesses such as Credit Card companies, cable service providers, SASS and telecommunication companies worldwide. Even though it is not the most fun to look at, customer churn metrics can help businesses improve customer retention.
    </h6>
''', unsafe_allow_html=True)


