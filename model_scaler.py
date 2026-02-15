# -*- coding: utf-8 -*-
"""
Created on Fri Feb 13 20:48:10 2026

@author: DELL
"""

import joblib
import streamlit as st

def load_model_and_scaler(model_path, scaler_path):
    try:
        model = joblib.load(model_path)
        scaler = joblib.load(scaler_path)
        return model, scaler
    except Exception as e:
        st.error(f"There's a problem with the model or the scaler: {e}")
        return None, None