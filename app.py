import streamlit as st
import pickle

with open('LoanPredictionModel','rb') as f:
    lr_model = pickle.load(f)

with open('LoanPredictionPickleModel','rb') as f:
    scaler_model = pickle.load(f)

st.title('Loan Prediction Model')

Employed,no_of_dependents = st.columns(2)
income_annual,loan_amount,loan_term = st.columns(3)
residential_assets_value,cibil_score =  st.columns(2)

no_of_dependents = no_of_dependents.number_input('Number of dependent Member',min_value=0 , max_value= 10,step = 1)
income_annual = income_annual.number_input('Annual Income',min_value=0,step = 1000)
loan_amount = loan_amount.number_input('Loan Amount',min_value=0,step = 1000)
loan_term = loan_term.number_input('Loan Term (year)',max_value = 20,min_value = 1,step = 1)
cibil_score = cibil_score.number_input('CIBIL Score',max_value = 900,min_value = 300,step = 50) 
residential_assets_value = residential_assets_value.number_input('Residential Assets',min_value=0,step = 1000)
Employed = Employed.selectbox('Employment Status',['Employed','Unemployed'] )

Employed = 1 if Employed == 'Employed' else 0

if st.button('Predict'):
    listOfFeatures = [no_of_dependents, income_annual, loan_amount, loan_term, cibil_score, residential_assets_value,  Employed,0]
    
    scaler_data = scaler_model.transform([listOfFeatures])
    scaler_data = scaler_data[:,:7]

    if lr_model.predict(scaler_data):
        st.success('Approved')
    else:
        st.error('Rejected')

