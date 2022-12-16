import streamlit as st
from database import get_employee_duty, getEmpName, insert_duty,get_employee_duty,promo_back
from database import new_Sal
def promo():
    employee_name=getEmpName()
    new=[]
    ssn=[]
    for i in employee_name:
        new.append(i[0])
        ssn.append(i[1])
    col1,col2= st.columns(2)
    with col1:
        selected_emp= st.selectbox("Employee you wish to give raise to:", new)
        if selected_emp:
            ind=new.index(selected_emp)
            ssn2=ssn[ind]
            data=promo_back(ssn2)
            data=data[0][0]
            if(data=='Not Elligible'):
                st.warning(str(selected_emp)+ " is not elligible for raise")
            else:
                st.success(str(data)+" can be given a raise!")
                st.subheader("How much do you wish to increase salary by: ")
                raise_amt=st.slider('Raise:', min_value=0, max_value=50, value=1, step=5)
                if(st.button("Give Raise")):
                    newSal=new_Sal(ssn2,raise_amt)
                    st.success("New salary of "+str(data)+" is "+str(newSal[0][0]))
                
