import streamlit as st
import joblib
import pandas as pd

# Carregar modelo e colunas
model = joblib.load('loan_model.pkl')
model_columns = joblib.load('model_columns.pkl')

# Função para previsão
def predict_loan_status(input_data):
    prediction = model.predict(input_data)[0]
    return "Aprovado" if prediction == 'Y' else "Não Aprovado"

# Interface do Streamlit
st.title('Simulador de Aprovação de Empréstimo')

# Inputs do usuário
st.header("Informações do Cliente")

# Dados numéricos
applicant_income = st.number_input('Renda do Requerente', min_value=0)
coapplicant_income = st.number_input('Renda do Cônjuge', min_value=0)
loan_amount = st.number_input('Valor do Empréstimo', min_value=0)
loan_term = st.number_input('Prazo do Empréstimo (meses)', min_value=0)
credit_history = st.selectbox('Histórico de Crédito', options=[1.0, 0.0])

# Dados categóricos
gender = st.selectbox('Gênero', ['Male', 'Female'])
married = st.selectbox('Casado(a)', ['Yes', 'No'])
education = st.selectbox('Educação', ['Graduate', 'Not Graduate'])
self_employed = st.selectbox('Autônomo', ['Yes', 'No'])
property_area = st.selectbox('Localização do Imóvel', ['Urban', 'Rural', 'Semiurban'])

# Criar DataFrame com os inputs
input_dict = {
    'Gender': [gender],
    'Married': [married],
    'Education': [education],
    'Self_Employed': [self_employed],
    'ApplicantIncome': [applicant_income],  # Verifique o nome exato da coluna
    'CoapplicantIncome': [coapplicant_income],
    'LoanAmount': [loan_amount],
    'Loan_Amount_Term': [loan_term],
    'Credit_History': [credit_history],
    'Property_Area': [property_area]
}

input_df = pd.DataFrame(input_dict, columns=model_columns)

# Botão de previsão
if st.button('Verificar Aprovação'):
    result = predict_loan_status(input_df)
    st.subheader(f'Resultado: {result}')
    st.write(input_df)  # Opcional: mostrar dados inseridos