import streamlit as st
import pandas as pd
from database import get_employee, get_employee_duty

def employee():
    result=get_employee()
    df = pd.DataFrame(result, columns=['First Name', 'Last Name', 'Start_date','SSN', 'Sex','Salary'])
    duty=get_employee_duty()
    with st.expander('Current employees: '):
        st.dataframe(df)
    
