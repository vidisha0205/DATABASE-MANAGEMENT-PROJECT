import mysql.connector
import streamlit as st
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="PROJECT"
)
c = mydb.cursor()
def add_data(Customer_Name, Customer_SSN, Customer_no, Customer_Location, Customer_City,Customer_PlantName,Customer_Count,Customer_PotSize,Customer_OrderID,Customer_DoO,Customer_DoA,Customer_Price):
    c.execute('INSERT IGNORE INTO CUSTOMER_ORDER VALUES(%s,%s)',(Customer_SSN, Customer_OrderID))
    mydb.commit()
    c.execute('INSERT IGNORE INTO CUSTOMER_DETAILS VALUES (%s,%s,%s)',( Customer_SSN, Customer_Name,Customer_no))
    mydb.commit()
    c.execute('INSERT IGNORE INTO ORDERS VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)',(Customer_Location, Customer_City,Customer_PlantName,Customer_OrderID,Customer_Count,Customer_DoA,Customer_PotSize,Customer_DoO,Customer_Price))
    mydb.commit()
    
def view_all_data():
    c.execute('SELECT Order_ID,Customer_Name,Plant_Name, Pot_Size, Price FROM ORDERS NATURAL JOIN CUSTOMER_DETAILS NATURAL JOIN CUSTOMER_ORDER')
    data = c.fetchall()
    return data
def view_only_customer_names():
    c.execute('SELECT Customer_Name FROM CUSTOMER_DETAILS')
    data = c.fetchall()
    return data
def get_order(c_name):
    c.execute('SELECT Order_ID, Customer_Name,Sci_Name, Com_Name, Count, Pot_Size, Price FROM ORDERS NATURAL JOIN CUSTOMER_ORDER NATURAL JOIN CUSTOMER_DETAILS INNER JOIN  TAXONOMY ON ORDERS.Plant_Name=TAXONOMY.Sci_Name WHERE Customer_Name="{}"'.format(c_name))
    data = c.fetchall()
    return data
def edit_order(new_Plant_Name, new_Count, new_Price, new_PotSize,Order_ID):
    c.execute("UPDATE ORDERS SET Plant_Name=%s, Count=%s, PRICE=%s, Pot_Size=%s WHERE Order_ID=%s", (new_Plant_Name,  new_Count, new_Price, new_PotSize, Order_ID))
    mydb.commit()
    c.execute('SELECT * FROM ORDERS WHERE Order_ID="{}"'.format(Order_ID))
    data = c.fetchall()
    return data
def insert_duty(duty,ssn,aisle):
    c.execute('INSERT IGNORE INTO DUTY VALUES(%s,%s,%s)',(duty,ssn,aisle))
    mydb.commit()
    
def delete_data(Order_ID,Cust_Name):
    c.execute('DELETE FROM ORDERS WHERE Order_ID="{}"'.format(Order_ID))
    mydb.commit()
    c.execute('DELETE FROM CUSTOMER_DETAILS WHERE Customer_Name="{}" LIMIT 1'.format(Cust_Name))
    mydb.commit()
    c.execute('DELETE FROM CUSTOMER_ORDER WHERE Order_ID="{}"'.format(Order_ID))
    mydb.commit()
    
def delete_data_user(Customer_Name):
    c.execute('SELECT Order_ID FROM  CUSTOMER_ORDER NATURAL JOIN CUSTOMER_DETAILS WHERE CUSTOMER_DETAILS.Customer_Name="{}"'.format(Customer_Name))
    data=c.fetchall()
    delete_data(data,Customer_Name)
    mydb.commit()
    return data
def get_plants():
    c.execute('SELECT DISTINCT Com_Name FROM TAXONOMY NATURAL JOIN PLANT')
    data=c.fetchall()
    return data

def get_Scientific_Name(Sname):
    c.execute('SELECT Sci_Name FROM TAXONOMY WHERE Com_Name="{}"'.format(Sname))
    data=c.fetchall()
    return data
def get_OrderID():
    c.execute('SELECT DISTINCT Order_ID FROM ORDERS')
    data=c.fetchall()
    return data

def get_employee():
    c.execute('SELECT * FROM EMPLOYEE')
    data=c.fetchall()
    return data

def get_employee_duty():
    c.execute('select service, Fname, Lname, Aisle_number from duty inner join employee on employee.SSN=duty.ESSN;')
    data=c.fetchall()
    return data

def getEmpName():
    c.execute('SELECT CONCAT(Fname," ",Lname),SSN FROM EMPLOYEE')
    data=c.fetchall()
    return data
def get_employee_duty_specific(ssn):
    c.execute('select service from duty inner join employee on employee.SSN=duty.ESSN WHERE employee.SSN="{}"'.format(ssn))
    data=c.fetchall()
    return data

def remove_service(ssn,duty):
    c.execute('DELETE FROM DUTY WHERE ESSN="{}" AND Service="{}"'.format(ssn,duty))
    
def insertEmp(Emp_fname,Emp_lname, Emp_SSN,Emp_start,Emp_Gender,Duty,aisle):
    c.execute('INSERT INTO EMPLOYEE VALUES(%s,%s,%s,%s,%s,%s)',(Emp_fname,Emp_lname,Emp_start,Emp_SSN,Emp_Gender,"15000"));
    mydb.commit()
    c.execute('INSERT INTO DUTY VALUES(%s,%s,%s)',(Duty,Emp_SSN,aisle))
    mydb.commit()
    
def promo_back(ssn):
    c.execute('SELECT Promotion("{}")'.format(ssn));
    data=c.fetchall()
    return data

def get_Sal(ssn):
    c.execute('SELECT SALARY FROM EMPLOYEE WHERE SSN="{}"'.format(ssn));
    data=c.fetchall()
    return data
def new_Sal(ssn,percent):
    c.execute('CALL Salary("{}","{}")'.format(ssn,percent));
    mydb.commit()
    data=get_Sal(ssn)
    return data
def add_data_pend(Plant_Name,Pot_Size,Count, Source_City,DoA,Dest_City):
    c.execute('INSERT INTO PENDING_ARRIVALS VALUES(%s,%s,%s,%s,%s,%s)',(Plant_Name,Pot_Size,Count,Source_City,DoA,Dest_City))
    c.execute('SELECT * FROM PENDING_ARRIVALS')
    data=c.fetchall()
    return data
