#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 11:06:33 2024

@author: m1.thibsuda
"""
import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the model open('filepath/filename','rb')
heartdisease_model = pickle.load(open('heartdisease_model.sav', 'rb'))
#create sidebar set default_index 0 = the first bar on the slidebar
with st.sidebar:
    selected = option_menu('Heart Disease Prediction System using ML',
                           ['Heart Disease Prediction',
                           'Info'],
                           icons=['heart','book'],
                           default_index=0)

# heart disease prediction page
if (selected == 'Heart Disease Prediction'):
    
    #page title
    st.title('Heart Disease Prediction using Machine Learning')
    
    #getting the input data from the user
    #columns for input fields (fucntion to layout on streamlit)
    col1, col2, col3 =st.columns(3)
    
    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Sex:(1 = male; 0 = female)')
    with col3:
        cp = st.text_input('Chest Pain types')
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl :(1 = true; 0 = false)')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
    

    
    
    
    #code for prediction
    heart_dignosis = ''
    
    
    #creating a button for prediction
    #1. name a button condition 
    if st.button('Heart Disease Test Result'):
        #pass the value inside the model saved.dubble squar bastket becuse be oredict a list in one person
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]
        
        #covert float value input
        user_input = [float(x) for x in user_input]
        
        heart_prediction = heartdisease_model.predict([user_input])
        #create another if condition for the result 
        if(heart_prediction[0]==0):
              heart_dignosis = 'Algorithm predict the person does not have any heart disease'
        else:
              heart_dignosis = 'Algorithm predict the person is having heart disease'
              
    st.success(heart_dignosis)

# Infomation
if selected == "Info":

    # page title
    st.title("Data dictionary")
