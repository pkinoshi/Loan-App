# -*- coding: utf-8 -*-
"""
Created on Sat Feb 14 20:29:08 2026

@author: DELL
"""

import streamlit as st

from model_scaler import load_model_and_scaler
from prediction_page import render_prediction_page
from methodology_page import render_methodology_page

def main():
    bread, beans = load_model_and_scaler("random_forest.joblib", "scaler.joblib")
    
    if bread and beans:
        st.sidebar.title("Splendor Analytics Loan App")
        
        if "page" not in st.session_state:
            st.session_state.page = "Predictor"
            
            
        if st.sidebar.button("Predictor"):
            st.session_state.page = "Predictor"
        
        if st.sidebar.button("Methodology"):
            st.session_state.page = "Methodology"
            
            
            
            
        if st.session_state.page == "Predictor":
            render_prediction_page(bread, beans)
        elif st.session_state.page == "Methodology":
            render_methodology_page()
            
        


main()            