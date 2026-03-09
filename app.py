import streamlit as st
import pickle
import pandas as pd
import sklearn
import numpy as np


pipe=pickle.load(open('pipe.pkl','rb'))
spcar=pd.read_csv('pspcar.csv')
spcar.head()

st.title('Car Price Prediction System')


model=st.selectbox('Enter the car model:',spcar['Car Model'].unique())
year=st.selectbox('Enter the year:',spcar['Year'].unique())
engine=st.selectbox('Enter the Engine Size (L):',spcar['Engine Size (L)'].unique())
horsepower=st.selectbox('Enter the Horsepower:',spcar['Horsepower'].unique())
torque=st.selectbox('Enter the Torque:',spcar['Torque (lb-ft)'].unique())
mph=st.selectbox('Enter 0-60 MPH Time (seconds):',spcar['0-60 MPH Time (seconds)'].unique())

predicted=pipe.predict(pd.DataFrame([[model,year,engine,horsepower,torque,mph]],columns=['Car Model','Year','Engine Size (L)','Horsepower','Torque (lb-ft)','0-60 MPH Time (seconds)']))

if st.button('Predict Price'):
    st.write('The Predicted Price is',predicted[0],'USD')