 
import pickle
import streamlit as st
 
# loading the trained model
pickle_in = open('classifier.pkl', 'rb') 
classifier = pickle.load(pickle_in)
 
@st.cache()


# defining the function which will make the prediction using the data which the user inputs 

def prediction(loan_amnt,term,int_rate,installment,sub_grade,home_ownership
                ,annual_inc,verification_status,purpose,dti,earliest_cr_line,
                open_acc,pub_rec,revol_bal,revol_util,total_acc,initial_list_status,
                application_type, mort_acc, pub_rec_bankruptcies):   
   
    # Pre-processing user input
    #sub_grade
    if sub_grade == "A1":
        sub_grade = 1
    elif sub_grade == "A2":
        sub_grade = 2
    elif sub_grade == "A3":
        sub_grade = 3
    elif sub_grade == "A4":
        sub_grade = 4
    elif sub_grade == "A5":
        sub_grade = 5
    elif sub_grade == "B1":
        sub_grade = 6
    elif sub_grade == "B2":
        sub_grade = 7
    elif sub_grade == "B3":
        sub_grade = 8
    elif sub_grade == "B4":
        sub_grade = 9
    elif sub_grade == "B5":
        sub_grade = 10
    elif sub_grade == "C1":
        sub_grade = 11
    elif sub_grade == "C2":
        sub_grade = 12
    elif sub_grade == "C3":
        sub_grade = 13
    elif sub_grade == "C4":
        sub_grade = 14
    elif sub_grade == "C5":
        sub_grade = 15
    elif sub_grade == "D1":
        sub_grade = 16
    elif sub_grade == "D2":
        sub_grade = 17
    elif sub_grade == "D3":
        sub_grade = 18
    elif sub_grade == "D4":
        sub_grade = 19
    elif sub_grade == "D5":
        sub_grade = 20
    elif sub_grade == "E1":
        sub_grade = 21
    elif sub_grade == "E2":
        sub_grade = 22
    elif sub_grade == "E3":
        sub_grade = 23
    elif sub_grade == "E4":
        sub_grade = 24
    elif sub_grade == "E5":
        sub_grade = 25
    elif sub_grade == "F1":
        sub_grade = 26
    elif sub_grade == "F2":
        sub_grade = 27
    elif sub_grade == "F3":
        sub_grade = 28
    elif sub_grade == "F4":
        sub_grade = 29
    elif sub_grade == "F5":
        sub_grade = 30
    elif sub_grade == "G1":
        sub_grade = 31
    elif sub_grade == "G2":
        sub_grade = 32
    elif sub_grade == "G3":
        sub_grade = 33
    elif sub_grade == "G4":
        sub_grade = 34
    elif sub_grade == "G5":
        sub_grade = 35
    else:
        sub_grade = 5

     #verification_status
    if verification_status == "Not Verified":
        verification_status = 0
    elif verification_status == "Source Verified":
        verification_status = 1
    elif verification_status == "Verified":
        verification_status = 2
    else :
        verification_status = 2

    #application_type
    if application_type == "INDIVIDUAL":
        application_type = 0
    elif application_type == "JOINT":
        application_type = 1
    elif application_type == "DIRECT_PAY":
        application_type = 2
    else:
        application_type = 0

    #initial_list_status
    if initial_list_status == "w":
        initial_list_status = 0
    elif initial_list_status == "f":
        initial_list_status = 1
    else:
        initial_list_status = 0
        
    #purpose 
    if purpose == "vacation":
        purpose = 0
    elif purpose == "debt_consolidation":
        purpose = 1
    elif purpose == "credit_card":
        purpose = 2
    elif purpose == "home_improvement":
        purpose = 3
    elif purpose == "small_business":
        purpose = 4
    elif purpose == "major_purchase":
        purpose = 5
    elif purpose == "other":
        purpose = 6
    elif purpose == "medical":
        purpose = 7
    elif purpose == "wedding":
        purpose = 8
    elif purpose == "car":
        purpose = 9
    elif purpose == "moving":
        purpose = 10
    elif purpose == "house":
        purpose = 11
    elif purpose == "educational":
        purpose = 12
    elif purpose == "renewable_energy":
        purpose = 13
    else :
        purpose = 2

    #home_ownership
    if home_ownership == "RENT":
        home_ownership = 0
    elif home_ownership == "MORTGAGE":
        home_ownership = 1
    elif home_ownership == "OWN":
        home_ownership = 2
    elif home_ownership == "OTHER":
        home_ownership = 3
    else:
        home_ownership=3
 
    # Making predictions 
    prediction = classifier.predict( 
        [[loan_amnt,term,int_rate,installment,sub_grade,home_ownership
                ,annual_inc,verification_status,purpose,dti,earliest_cr_line,
                open_acc,pub_rec,revol_bal,revol_util,total_acc,initial_list_status,
                application_type, mort_acc, pub_rec_bankruptcies]])
     
    if prediction == 0:
        pred = 'Defaulter'
    else:
        pred = 'Loan Paid (No Dues Left)'
    return pred
      
  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color: #FFACAC;padding:13px"> 
    <h1 style ="color:black;text-align:center;">CreditAssure - TEAM RN</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    loan_amnt = st.number_input('TOTAL LOAN AMOUNT')
    term = st.selectbox('TERM',("36","60")) 
    int_rate= st.number_input("INTEREST RATE") 
    installment = st.number_input("INSTALLMENT")
    sub_grade= st.selectbox('SUBGRADE',("A1","A2","A3","A4","A5","B1","B2","B3","B4",
                                                         "B5","C1","C2","C3","C4","C5","D1","D2","D3","D4","D5","E1",
                                                        "E2","E3","E4","E5","G1","G2","G3","G4","G5"))
    home_ownership= st.selectbox('HOME OWNERSHIP',("RENT","MORTGAGE","OWN","OTHER"))
    annual_inc= st.number_input("ANNUAL INCOME")
    verification_status = st.selectbox('VERIFICATION STATUS',("Not Verified","Source Verified","Verified"))
    purpose = st.selectbox('PUPROSE OF LOAN',("vacation","debt_consolidation","credit_card","home_improvement","small_business","major_purchase","other","medical","wedding","car","moving","house","educational","renewable_energy"))
    dti = st.slider("DEBT TO INCOME RATIO", min_value=0, max_value=100, value=50, step=1)
    earliest_cr_line = st.number_input("CREDIT AGE")
    open_acc = st.number_input("NUMBER OF OPEN ACCOUNTS")
    pub_rec = st.number_input("NUMBER DEROGATORY PUBLIC RECORDS")
    revol_bal = st.number_input("REVOLVING BALANCE ")
    revol_util = st.number_input("REVOLVING LINE UTILIZATION RATE")
    total_acc = st.number_input("CREDIT ACCOUNTS")
    initial_list_status = st.selectbox('INITIAL LIST STATUS',("w","f"))
    application_type = st.selectbox('LOAN APPLICATION STATUS',("INDIVIDUAL","JOINT","DIRECT_PAY"))
    mort_acc = st.number_input("NUMBER OF MORTGAGE ACCOUNTS")
    pub_rec_bankruptcies = st.number_input("NUMBER OF PUBLIC RECORD BANKRUPTICIES")
    
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(loan_amnt,term,int_rate,installment,sub_grade,home_ownership
                ,annual_inc,verification_status,purpose,dti,earliest_cr_line,
                open_acc,pub_rec,revol_bal,revol_util,total_acc,initial_list_status,
                application_type, mort_acc, pub_rec_bankruptcies) 
        st.success(result)
        
     
if __name__=='__main__': 
    main()
