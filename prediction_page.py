# -*- coding: utf-8 -*-
"""
Created on Fri Feb 13 21:22:07 2026

@author: DELL
"""

import streamlit as st
from preprocessing_file import preprocess_input

def render_prediction_page(model, scaler):
    st.title("Loan Eligibity Predictor.")
    st.write("Provide applicant details to evaluate loan status.")
    
    with st.container():
        col1, col2 = st.columns(2)
        
        with col1:
            gender = st.selectbox("Gender", ["Male", "Female"])
            married = st.selectbox("Married", ["Yes", "No"])
            dependents = st.slider("Number of Dependents", 0, 3, 0)
            education = st.selectbox("Education Level", ["Graduate", "Not Graduate"])
            self_employed = st.selectbox("Self-Employed", ["No", "Yes"])
            property_area = st.selectbox("Property Area", ["Urban", "Rural", "Semiurban"])
        with col2:
            income = st.number_input("Applicant Income (Thousands)", min_value=0, value=0)
            co_income = st.number_input("Coapplicant Income (Thousands)", min_value=0, value=0)
            loan_amt = st.number_input("Loan Amount", min_value=0, value=0)
            loan_term = st.selectbox("Loan Term (Days)", [12, 36, 60, 84, 120, 180, 240, 300, 360, 480])
            credit_history = st.radio("Credit Histroy", [1.0, 0.0], help="1.0 = Good, 0.0 = Poor.")
            
            
        #Income binning logic
        if income <= 2500:
            income_val = 2 #Very Low
        elif income <= 5000:
            income_val = 1 #Low
        elif income <= 10000:
            income_val = 0 #Moderate
        elif income <= 20000:
            income_val = 3 #High
        elif income <= 40000:
            income_val = 4 #Very High
        else:
            income_val = 5 #Ultra High
            
                
        if st.button("Make Prediction"):
            input_raw = {
                    "Gender":gender, "Married":married, "Dependents":dependents, "Education":education,
                    "Self_Employed":self_employed, "Property_Area":property_area, "ApplicantIncome":income, 
                    "CoapplicantIncome":co_income,
                    "LoanAmount":loan_amt, "Loan_Amount_Term":loan_term, "Credit_History":credit_history,
                    "IncomeBin":income_val
                }
            
            features = preprocess_input(input_raw)
            scaled_features = scaler.transform(features)
                
            predictions = model.predict(scaled_features)
            
            if predictions[0] == 0:
                st.balloons()
                st.success("Prediction: Approved(Y)")
            else:
                st.error("Prediction: Rejected(N)")