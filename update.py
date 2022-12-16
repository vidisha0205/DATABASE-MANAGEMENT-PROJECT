import pandas as pd
import streamlit as st
from database import view_all_data, view_only_customer_names, get_order, edit_order,get_plants, get_Scientific_Name
def update():
    plants=get_plants()
    ans=[]
    for i in plants:
        ans.append(str(i)[2:-3:])
    result = view_all_data()
    df = pd.DataFrame(result, columns=['Order ID', 'Customer Name', 'Plant Name','Pot Size', 'Price'])
    with st.expander("Current Orders"):
        st.dataframe(df)
        list_of_customer_names = [i[0] for i in view_only_customer_names()]
        selected_c = st.selectbox("Customer order to edit:", list_of_customer_names)
        selected_result = get_order(selected_c)
        if selected_result:
            Order_ID = selected_result[0][0]
            Customer_Name = selected_result[0][1]
            Plant_Name = selected_result[0][2]
            Count= selected_result[0][3]
            Price = selected_result[0][4]
            col1,col2 = st.columns(2)
            with col1:
                new_Plant_Name= st.selectbox("Plant:",ans)
                new_Count = st.slider('Count:', min_value=1, max_value=20, value=1, step=1)
                new_Price=st.text_input("Amount:")
                new_PotSize=st.selectbox("Pot Size", ["L","M","S"])
                if st.button("Update Order"):
                    new_Plant_Name=get_Scientific_Name(new_Plant_Name)
                    new_Plant_Name=str(new_Plant_Name)[3:-4:]
                    edit_order(new_Plant_Name, new_Count, new_Price,new_PotSize, Order_ID)
                    st.success("Successfully updated")
                    result2 = view_all_data()
                    df2 = pd.DataFrame(result2, columns=['Order ID', 'Customer Name', 'Plant Name','Pot Size', 'Price'])
                    with st.title("Updated Order"):
                        st.dataframe(df2)
            with col2:
                st.title("UPDATION IN PROCESS")
