import pandas as pd
import streamlit as st
from database import view_all_data, view_only_customer_names, delete_data_user, get_order

def order_cust():
    result=view_only_customer_names()
    df=pd.DataFrame(result, columns=['Customers'])
    with st.expander("Your Orders: "):
        st.dataframe(df)
        list_of_customers = [i[0] for i in view_only_customer_names()]
        selected_customer = st.selectbox("User Name:", list_of_customers)
        if st.button("Show Orders"):
            newdf=get_order(selected_customer)
            df2 = pd.DataFrame(newdf, columns=['Order ID', 'Customer Name', 'Scientific name','Plant Name', 'Count', 'Pot Size', 'Price'])
            with st.title("Your Orders"):
                st.dataframe(df2)
