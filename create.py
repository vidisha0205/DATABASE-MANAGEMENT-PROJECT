import streamlit as st
from database import add_data, get_plants, get_Scientific_Name, get_OrderID
import random
import string

def create():
    plants=get_plants()
    ans=[]
    for i in plants:
        ans.append(str(i)[2:-3:])
    orders=get_OrderID()
    newOrd=[]
    for i in orders:
        newOrd.append(str(i)[2:-3:])
    N=random.randint(5,10)
    custord='TY7C4Q'
    while(custord in newOrd):
        custord=''.join(random.choices(string.ascii_uppercase+string.digits,k=N))
    newOrd.append(custord)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        Customer_Name = st.text_input("Name:")
        Customer_SSN = st.text_input("SSN:")
        Customer_no=st.text_input("Contact Number:")   
        if(len(Customer_no)<=10 and (len(Customer_SSN)==9 or len(Customer_SSN)==0)):
                with col2:
                    Customer_City = st.selectbox("City", ["Bangalore", "Chennai", "Mumbai","Delhi","Kharagpur","Hyderabad"])
                    Customer_Location = st.text_input("Location:")
                with col3:
                    Customer_PlantName = st.selectbox("Plant:",ans)
                    Customer_Count = st.slider('Count:', min_value=1, max_value=20, value=1, step=1)
                    Customer_PotSize=st.selectbox("Pot Size", ["L","M","S"])
                with col4:
                    Customer_OrderID=st.text_input("Order ID: ",custord)
                    Customer_DoO=st.date_input("Date of Order:")
                    Customer_DoA=st.date_input("Expected date of Delivery:")        
                    Customer_Price=st.text_input("Amount:")        
                if st.button("Add Order"):
                    Customer_PlantName=get_Scientific_Name(Customer_PlantName)
                    Customer_PlantName=str(Customer_PlantName)[3:-4:]
                    st.title(Customer_PlantName)
                    add_data(Customer_Name, Customer_SSN, Customer_no, Customer_Location, Customer_City,
                             Customer_PlantName,Customer_Count,Customer_PotSize,Customer_OrderID,
                             Customer_DoO,Customer_DoA,Customer_Price)
                    st.success("Successfully added order from Customer: {}".format(Customer_Name))
        else:
            if(len(Customer_no)>10):
                   st.warning("Invalid Phone Number")
            else:
                 st.warning("Invalid SSN")   
            

