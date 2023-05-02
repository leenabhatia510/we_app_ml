import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loadibg the saved models

creditcard_model = pickel.load(open('creditcard_model.sav', 'rb'))


# sidebar for navigation
with st.sideBar:
    selected = option_menu('Online Fraud Detection System',
                           
                           ['Credit card Fraud'],
                           icons=['money'],
                           default_index=0)
    
# credit card detection page
if (selected == 'Credit card Fraud'):

    #page title
    st.title('Credit Card Fraud using ML')

    #getting the input data from the user
    col1, col2, col3, col4 = st.columns(4)

    with col1: 
        V1 = st.text_input('Transaction Feature value  V1')

    with col1: 
        V2 = st.text_input('Transaction Feature value  V2')

    with col1: 
        V3 = st.text_input('Transaction Feature value  V3')
  
    with col1: 
        V4 = st.text_input('Transaction Feature value  V4')

    with col1: 
        V5 = st.text_input('Transaction Feature value  V5')

    with col1: 
        V6 = st.text_input('Transaction Feature value  V6')

    with col1: 
        V7 = st.text_input('Transaction Feature value  V7')

    with col2: 
        V8 = st.text_input('Transaction Feature value  V1')

    with col2: 
        V9 = st.text_input('Transaction Feature value  V2')

    with col2: 
        V10 = st.text_input('Transaction Feature value  V3')
  
    with col2: 
        V11 = st.text_input('Transaction Feature value  V4')

    with col2: 
        V12 = st.text_input('Transaction Feature value  V5')

    with col2: 
        V13 = st.text_input('Transaction Feature value  V6')

    with col2: 
        V14 = st.text_input('Transaction Feature value  V7')

    with col3: 
        V15 = st.text_input('Transaction Feature value  V1')

    with col3: 
        V16 = st.text_input('Transaction Feature value  V2')

    with col3: 
        V17 = st.text_input('Transaction Feature value  V3')
  
    with col3: 
        V18 = st.text_input('Transaction Feature value  V4')

    with col3: 
        V19 = st.text_input('Transaction Feature value  V5')

    with col3: 
        V20 = st.text_input('Transaction Feature value  V6')

    with col3: 
        V21 = st.text_input('Transaction Feature value  V7')

    with col4: 
        V22 = st.text_input('Transaction Feature value  V1')

    with col4: 
        V23 = st.text_input('Transaction Feature value  V2')

    with col4: 
        V24 = st.text_input('Transaction Feature value  V3')
  
    with col4: 
        V25 = st.text_input('Transaction Feature value  V4')

    with col4: 
        V26 = st.text_input('Transaction Feature value  V5')

    with col4: 
        V27 = st.text_input('Transaction Feature value  V6')

    with col4: 
        V28 = st.text_input('Transaction Feature value  V7')

    with col4: 
        classV = st.text_input('Class Value')


# code for detection
fraud_detection = ''

# creating a button for prediction

if st.button('Whether the transactio is legit aur fraudulent'):
    fraud_prediction = creditcard_model.predict([classV])

    if (fraud_prediction[0] == 0):
        fraud_detection = 'The transaction is Legit'
    else:
        fraud_detection = 'The Transaction is fraudulent'

st.success(fraud_detection)