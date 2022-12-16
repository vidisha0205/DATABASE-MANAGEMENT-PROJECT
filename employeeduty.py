import pandas as pd
import streamlit as st
import plotly.express as px
from database import view_all_data, get_employee_duty, getEmpName, insert_duty,get_employee_duty,get_employee_duty_specific
def employee_duty():
    result=get_employee_duty()
    df = pd.DataFrame(result, columns=['Service','First Name', 'Last Name','Aisle Number'])
    with st.expander('Current employee Duties Are: '):
        st.dataframe(df)
        employee_name=getEmpName()
        new=[]
        ssn=[]
        for i in employee_name:
            new.append(i[0])
            ssn.append(i[1])
    selected_emp= st.selectbox("Employee you wish to edit:", new)
    if selected_emp:
            ind=new.index(selected_emp)
            ssn2=ssn[ind]
            list1=get_employee_duty_specific(ssn2)
            duty=[]
            for i in list1:
                duty.append(i[0])
            list1=get_employee_duty_specific(ssn2)
            duty=[]
            for i in list1:
                duty.append(i[0])
            L=["Composting","Cleaning","Planting","Watering","Soil Aeration","Pruning","Sales"]
            New=[]
            for i in L:
                if(i not in duty):
                    New.append(i)
            result=get_employee_duty_specific(ssn2)
            if(result):
                    df = pd.DataFrame(result, columns=['Service'])
                    with st.subheader('The Current Employee Duties Are: '):
                        st.dataframe(df)
            s_duty= st.selectbox(" Service you wish to add:",New)
            if(s_duty!="Sales"):
                aisle=st.selectbox("Aisle number:",list(range(1,5)))
            else:
                aisle=0
            if(st.button("Add Duty")):
                insert_duty(s_duty,ssn2,aisle)
                result=get_employee_duty_specific(ssn2)
                if(result):
                    df = pd.DataFrame(result, columns=['Service'])
                    with st.subheader('The Current Employee Duties Are: '):
                        st.dataframe(df)
            
            
            
