import streamlit as st
from database import insertEmp
import random
def NewEmp():
    col1,col2= st.columns(2)
    with col1:
        Emp_fname=st.text_input("Employee First Name: ")
        Emp_lname=st.text_input("Employee Last Name: ")
        Emp_SSN=st.text_input("Employee SSN: ")
        if(len(Emp_SSN)>9):
            st.warning("Invalid Phone Number")
    with col2:
        Emp_Start=st.date_input("Start Date:")
        Emp_Gender=st.selectbox("Sex",["M","F"])
        Q=[]
        L=["Composting","Cleaning","Watering","Soil Aeration","Pruning","Sales"]
        Emp_Duty=st.selectbox("Duties:",L)
        Aisle=random.randint(1,5)
        for i in L:
                if(i not in Q):
                        Q.append(i)
                        
    if(st.button("Add Employee")):
       insertEmp(Emp_fname,Emp_lname, Emp_SSN,Emp_Start,Emp_Gender,Emp_Duty,Aisle)
       st.success("Successfully added Employee: {}".format(Emp_fname+" "+Emp_lname))
