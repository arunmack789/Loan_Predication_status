import streamlit as st
import pickle
import numpy as np
import os
path = os.path.dirname(__file__)

model = pickle.load(open(path + '/rf_model.pt','rb'))

st.set_page_config(
    page_title="Loan Prediction App",
    page_icon="🏦",
    layout="centered",
    initial_sidebar_state="expanded",
)

from PIL import Image
image = Image.open(path + '/loanapp.jpg')

st.image(image,use_column_width=True)

def predict_loan_status(loanamount,credithistory,applicantincome,dependents):
    input=np.array([[loanamount,credithistory,applicantincome,dependents]]).astype(int)
    prediction = model.predict(input)
    #pred = '{0:.{1}f}'.format(prediction[0][0], 2)
    return int(prediction)


def main():
    #st.title("Abalone Age Prediction")
    html_temp = """
    <div style="background:#4B3869 ;padding:10px">
    <h2 style="color:white;text-align:center;">Loan  Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html = True)

    LoanAmount = st.text_input("Loan Amount")
    Credit_History = st.selectbox("Credit History",[0,1])
    ApplicantIncome = st.text_input("Applicant Income")
    Dependents = st.radio('Dependents', [0,1,2,3])


    safe_html ="""  
      <div style="background-color:#80ff80; padding:10px >
      <h2 style="color:white;text-align:center;"> Loan Status is not Approved</h2>
      </div>
    """
    warn_html ="""  
      <div style="background-color:#F4D03F; padding:10px >
      <h2 style="color:white;text-align:center;"> Loan Status is APPROVED</h2>
      </div>
    """
    danger_html="""  
      <div style="background-color:#F08080; padding:10px >
       <h2 style="color:black ;text-align:center;"> The Abalone is old</h2>
       </div>
    """
    if st.button("Predict Loan Status"):
            output = predict_loan_status(LoanAmount,Credit_History,ApplicantIncome,Dependents)
            st.success('The Loan Status is {}'.format(output))

            if output == 0:
                st.markdown(safe_html,unsafe_allow_html=True)
            elif output == 1:
                st.markdown(warn_html,unsafe_allow_html=True)
            # elif output == 3:
            #     st.markdown(danger_html,unsafe_allow_html=True)

if __name__=='__main__':
    main()
