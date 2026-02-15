# -*- coding: utf-8 -*-
"""
Created on Fri Feb 13 20:59:08 2026

@author: DELL
"""

import pandas as pd

def preprocess_input(data_dict):
    mappings = {
            "Gender": {'Male': 0, 'Female': 1},
            "Married": {'No': 0, 'Yes': 1},
            "Education": {'Graduate': 0, 'Not Graduate': 1},
            "Self_Employed": {'No': 0, 'Yes': 1},
            "Property_Area": {'Urban': 0, 'Rural': 1, 'Semiurban': 2}
        }
    
    processed_data = {
            "Gender": mappings["Gender"][data_dict["Gender"]],
            "Married": mappings["Married"][data_dict["Married"]],
            "Dependents": float(data_dict["Dependents"]),
            "Education": mappings["Education"][data_dict["Education"]],
            "Self_Employed": mappings["Self_Employed"][data_dict["Self_Employed"]],
            "ApplicantIncome": data_dict["ApplicantIncome"],
            "CoapplicantIncome": data_dict["CoapplicantIncome"],
            "LoanAmount": data_dict["LoanAmount"],
            "Loan_Amount_Term": data_dict["Loan_Amount_Term"],
            "Credit_History": data_dict["Credit_History"],
            "Property_Area": mappings["Property_Area"][data_dict["Property_Area"]],
            "IncomeBin": data_dict["IncomeBin"]
        }
    return pd.DataFrame([processed_data])