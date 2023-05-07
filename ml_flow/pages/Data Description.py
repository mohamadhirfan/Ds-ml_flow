import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import os
import matplotlib.pyplot as plt


FILE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
dir_of_interest = os.path.join(PARENT_DIR, "resources")

DATA_PATH = os.path.join(dir_of_interest, 'data',"churn.csv")

st.markdown("""
    <style>
        body {
            background-image: url("https://tse3.mm.bing.net/th?id=OIP.vc1fl4tEOdU6uQzEU_tSHwHaFI&pid=Api&P=0");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
        .stApp {
            background-color: rgba(255, 255, 255, 0.1);
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='color:red;'>Data Visualization</h1>",unsafe_allow_html=True)

df = pd.read_csv(DATA_PATH)

st.write(df.describe())

st.bar_chart(df["Churn"].value_counts())

CHURN_Y = df[df['Churn']==1]
no_CHURN = df[df['Churn']==0]

fig, ax = plt.subplots()
sns.scatterplot(x=df['tenure'],y= df['TotalCharges'],hue=df['Churn'])

ax.set_xlabel('tenure')
ax.set_ylabel("TotalCharges")
ax.legend()
st.pyplot(fig)



labels = ['CHURN_Y', 'no_CHURN']
sizes = [34.2, 65.8]  
fig, ax = plt.subplots()
_, _, autotexts = ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax.axis('equal')
ax.set_title('Percentage of Churn Customers')

for autotext in autotexts:
    autotext.set_fontsize(12)

st.pyplot(fig)