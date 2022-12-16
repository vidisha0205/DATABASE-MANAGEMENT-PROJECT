import pandas as pd
import streamlit as st
import plotly.express as px
from database import remove_service, get_employee_duty, getEmpName, insert_duty,get_employee_duty,get_employee_duty_specific
def remove_duty():
    result=get_employee_duty()[2::]
    df = pd.DataFrame(result, columns=['Service','First Name', 'Last Name','Aisle Number'])
    with st.expander('Current employee Duties Are: '):
        st.dataframe(df)
        employee_name=getEmpName()
        new=[]
        ssn=[]
        for i in employee_name:
            new.append(i[0])
            ssn.append(i[1])
        selected_emp= st.selectbox("Employee whose service you wish to remove:", new)
        if selected_emp:
            ind=new.index(selected_emp)
            ssn2=ssn[ind]
            list1=get_employee_duty_specific(ssn2)
            duty=[]
            for i in list1:
                duty.append(i[0])
            selected_duty= st.selectbox("Service you wish to remove:", duty)
            if selected_duty:
                if(st.button("Delete Service")):
                    remove_service(ssn2,selected_duty)
                    result=get_employee_duty_specific(ssn2)
                    if(result):
                            df = pd.DataFrame(result, columns=['Service'])
                            st.subheader('The Current Employee Duties Are: ')
                            st.dataframe(df)
            
            
            
