from database import add_data_pend, get_plants, get_Scientific_Name
import random
import string
import pandas as pd
import streamlit as st
def pend():
    col1, col2= st.columns(2)
    plants=get_plants()
    ans=[]
    for i in plants:
        ans.append(str(i)[2:-3:])
    cities= ["Bangalore", "Chennai", "Mumbai","Delhi","Kannur","Bhopal","Anantpur","Latur","Kharagpur","Hyderabad"]
    with col1:
        Plant_Name = st.selectbox("Plant Name:",ans)
        Plant_Name=get_Scientific_Name(Plant_Name)
        Plant_Name=str(Plant_Name)[3:-4:]
        Pot_Size = st.selectbox("Size:",["L","M","S"])
        Count=st.slider("Count:",min_value=1, max_value=50, value=1, step=1)   
        with col2:
            Source_City = st.selectbox("Source City",cities)
            DoA=st.date_input("Expected date of Arrival:")
            Dest_City=st.selectbox("City", ["Bangalore", "Chennai", "Mumbai","Delhi","Kharagpur","Hyderabad"])
            if st.button("Add Order"):
                    result=add_data_pend(Plant_Name,Pot_Size,Count,Source_City,DoA,Dest_City)
                    st.success("Successfully added order for plant".format(Plant_Name))
                    df=pd.DataFrame(result, columns=['Plant Name', 'Pot Size', 'Count','Source', 'Date of Arrival','City'])
                    with st.expander('Pending Arrivals: '):
                        st.dataframe(df)


