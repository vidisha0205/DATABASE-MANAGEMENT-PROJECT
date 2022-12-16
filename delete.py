import pandas as pd
import streamlit as st
from database import view_all_data, view_only_customer_names, delete_data_user
def delete():
    result = view_all_data()
    df = pd.DataFrame(result, columns=['Order ID', 'Customer Name', 'Plant Name','Pot Size','Price'])
    with st.expander("Current Orders"):
        st.dataframe(df)
        list_of_customers = [i[0] for i in view_only_customer_names()]
        selected_customer = st.selectbox("Customer whose order to delete:", list_of_customers)
        st.warning("Do you want to delete your order?")
        if st.button("Delete Order"):
            delete_data_user(selected_customer)
            st.success("Order has been deleted successfully")
            new_result = view_all_data()
            df2 = pd.DataFrame(new_result, columns=['Order ID', 'Customer Name', 'Plant Name','Pot Size', 'Price'])
            with st.title("Updated Orders after deletion"):
                st.dataframe(df2)
