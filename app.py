#import mysql.connector
#mydb = mysql.connector.connect(
#    host="localhost",
#    user="root"
#)
#c = mydb.cursor()
#c.execute("USE PROJECT")
import streamlit as st
import pandas as pd
from create import create
from delete import delete
from read import read
from update import update
from sql import sql
from customer import order_cust
import plotly.express as px
from employee import employee
from employeeduty import employee_duty
from removeduty import remove_duty
from newEmp import NewEmp
from promo import promo
from pend import pend
def main():
    st.title("PLANT NURSERY MANAGEMENT SYSTEM")
    st.title("PES1UG20CS091")
    menu = ["Add Order", "View Order", "Edit Order", "Cancel Order","Your Orders","New Employee","Add Services","Remove Service","Promotions","Pending Arrivals","SQL Command"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Add Order":
        st.subheader("Enter Order Details:")
        create()
    elif choice == "View Order":
        st.subheader("View Orders:")
        read()
    elif choice == "Edit Order":
        st.subheader("Changed Order details")
        update()
    elif choice == "Cancel Order":
        st.subheader("Order Cancellation")
        delete()
    elif choice == "New Employee":
        st.subheader("Employment in Process")
        NewEmp()
    elif choice=="Your Orders":
        st.subheader("Your Orders With Us")
        order_cust()
    elif choice=="Employee Details":
        st.subheader("Current Emloyees")
        employee()
    elif choice=="Add Services":
        st.subheader("Employee Duties Are:")
        employee_duty()
    elif choice=="Remove Service":
        st.subheader("Employee Duties Are:")
        remove_duty()
    elif choice =="Promotions":
        st.subheader("Promotion time!")
        promo()
    elif choice=="Pending Arrivals":
        st.subheader("Pending Arrivals")
        pend()
    elif choice== 'SQL Command':
        st.subheader("Type in your Query")
        ans=sql()
        if(ans!=0):
                df = pd.DataFrame(ans)
                st.dataframe(df)
        else:
            st.subheader("No query given")
    else:
        st.subheader("About tasks")
        
if __name__ == '__main__':
    main()
