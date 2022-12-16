/*Creating Database*/
CREATE DATABASE PROJECT;
/*Using the Database*/
USE PROJECT;

/*Database Creation*/
CREATE TABLE PLANT_DETAILS(
    Plant_ID varchar(10) NOT NULL, 
    Sci_Name varchar(50) NOT NULL, 
    CONSTRAINT plant_details_prim PRIMARY KEY(Plant_ID,Sci_Name));

CREATE TABLE PLANT(
    Plant_ID varchar(10) NOT NULL,
    Plant_Aisle int, 
    Plantation_date DATE,PRIMARY KEY(Plant_ID), 
    FOREIGN KEY(Plant_ID) REFERENCES PLANT_DETAILS(PLANT_ID));

CREATE TABLE TAXONOMY(
    Sci_Name varchar(50) NOT NULL, 
    Com_Name varchar(50) NOT NULL,
    PRIMARY KEY(Sci_Name));

CREATE TABLE EMPLOYEE(
    FName varchar(20) NOT NULL, 
    LName varchar(20), 
    Start_date DATE, 
    SSN varchar(20) PRIMARY KEY, 
    Sex varchar(1));

CREATE TABLE LOCATION(
    Head_SSN varchar(20) NOT NULL, 
    Location_name varchar(20) NOT NULL,
    Head_of_Location varchar(10), 
    Year_est DATE, 
    PRIMARY KEY(Head_SSN, Location_name),
    FOREIGN KEY(Head_SSN) REFERENCES EMPLOYEE(SSN));

CREATE TABLE DUTY(
    Service varchar(20), 
    ESSN varchar(20) PRIMARY KEY, 
    Aisle_number int, 
    FOREIGN KEY(ESSN) REFERENCES EMPLOYEE(SSN));

CREATE TABLE TYPE_AVAILABILITY(
    Plant_ID varchar(10), 
    Type_Name varchar(10),
    Pot_Size varchar(1),
    PRIMARY KEY(Plant_ID, Type_Name), 
    FOREIGN KEY(Plant_ID) REFERENCES PLANT_DETAILS(Plant_ID));

CREATE TABLE CUSTOMER_ORDER(
    Customer_SSN varchar(20), 
    Order_ID varchar(10), 
    PRIMARY KEY(Customer_SSN, Order_ID));

CREATE TABLE CUSTOMER_DETAILS(
    Customer_SSN varchar(20) PRIMARY KEY, 
    Customer_Name varchar(20), 
    Contact_number int,
    FOREIGN KEY(Customer_SSN) REFERENCES CUSTOMER_ORDER(Customer_SSN));

CREATE TABLE ORDERS(
    Location varchar(20),
    Plant_Name varchar(20),
    Order_ID varchar(10) PRIMARY KEY, 
    Count int, Date_of_delivery DATE, 
    Pot_Size varchar(1), 
    Date_of_Order DATE, 
    PRICE int,
    FOREIGN KEY(Plant_Name) REFERENCES TAXONOMY(Sci_Name));

CREATE TABLE PENDING_ARRIVALS(
    Plant_Name varchar(50),
    Pot_Size varchar(1),
    Count int,
    Source varchar(20),
    Date_of_Arrival DATE,
    City varchar(20),
    PRIMARY KEY(Plant_Name,City),
    FOREIGN KEY(Plant_Name) REFERENCES TAXONOMY(Sci_Name));
/*Database Population*/
INSERT INTO TAXONOMY VALUES("Mangifera indica","Mango");

INSERT INTO PLANT_DETAILS VALUES 
("ZM01","Zea mays"),
("ZM02","Zea mays"), 
("TA01","Triticum aestivum"), 
("NI01","Nerium indicum"), 
("NI02","Nerium indicum"), 
("NI03","Nerium indicum"), 
("NI04","Nerium indicum"), 
("HA01","Helianthus annus"), 
("HA02","Helianthus annus"), 
("HA03","Helianthus annus"), 
("HA04","Helianthus annus"), 
("HA05","Helianthus annus"), 
("HA06","Helianthus annus"), 
("HR01","Hibiscus rosasinensis"), 
("HR02","Hibiscus rosasinensis"), 
("HR03","Hibiscus rosasinensis"), 
("HR04","Hibiscus rosasinensis");

LOAD DATA INFILE "type.csv" INTO TABLE TYPE_AVAILABILITY COLUMNS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' ESCAPED BY '"' LINES TERMINATED BY '\n' IGNORE 1 LINES;
LOAD DATA INFILE "taxonomy.csv" INTO TABLE TAXONOMY COLUMNS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' ESCAPED BY '"' LINES TERMINATED BY '\n' IGNORE 1 LINES;
LOAD DATA INFILE "cusdet.csv" INTO TABLE Customer_Details COLUMNS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' ESCAPED BY '"' LINES TERMINATED BY '\n' IGNORE 1 LINES;
LOAD DATA INFILE "cusord.csv" INTO TABLE Customer_Order COLUMNS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' ESCAPED BY '"' LINES TERMINATED BY '\n' IGNORE 1 LINES;
LOAD DATA INFILE "details.csv" INTO TABLE PLANT_DETAILS COLUMNS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' ESCAPED BY '"' LINES TERMINATED BY '\n' IGNORE 1 LINES;
LOAD DATA INFILE "duty.csv" INTO TABLE DUTY COLUMNS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' ESCAPED BY '"' LINES TERMINATED BY '\n' IGNORE 1 LINES;
LOAD DATA INFILE "type.csv" INTO TABLE TYPE_AVAILABILITY COLUMNS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' ESCAPED BY '"' LINES TERMINATED BY '\n' IGNORE 1 LINES;
LOAD DATA INFILE "taxonomy.csv" INTO TABLE TAXONOMY COLUMNS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' ESCAPED BY '"' LINES TERMINATED BY '\n' IGNORE 1 LINES;
LOAD DATA INFILE "PEND.csv" INTO TABLE PENDING_ARRIVALS COLUMNS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' ESCAPED BY '"' LINES TERMINATED BY '\n' IGNORE 1 LINES;
LOAD DATA INFILE "taxonomy.csv" INTO TABLE TAXONOMY COLUMNS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' ESCAPED BY '"' LINES TERMINATED BY '\n' IGNORE 1 LINES;
LOAD DATA INFILE "plant_details.csv" INTO TABLE PLANT COLUMNS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' ESCAPED BY '"' LINES TERMINATED BY '\n' IGNORE 1 LINES;
LOAD DATA INFILE "taxonomy.csv" INTO TABLE TAXONOMY COLUMNS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' ESCAPED BY '"' LINES TERMINATED BY '\n' IGNORE 1 LINES;
LOAD DATA INFILE "emp.csv" INTO TABLE EMPLOYEE COLUMNS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' ESCAPED BY '"' LINES TERMINATED BY '\n' IGNORE 1 LINES;
LOAD DATA INFILE "head.csv" INTO TABLE LOCATION COLUMNS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' ESCAPED BY '"' LINES TERMINATED BY '\n' IGNORE 1 LINES;

/* JOIN QUERIES */
/* 1). The Management wants a list of names of plants which are currently maintained, 
that are either Fruit or Vegetable. However, it does not have any need for the scientific name. 
Return the common names of such plants.*/
SELECT DISTINCT Com_Name
FROM PLANT_DETAILS NATURAL JOIN TYPE_AVAILABILITY NATURAL JOIN TAXONOMY 
WHERE Type_Name="Fruit" OR Type_Name="Vegetable";

/*2). You wish to know the quality of Mango plants that were bought from this nursery 
and hence want to ask every customer who bought mangoes, their review. 
Print the customer name and contact number of only those who bought Mango plants*/
SELECT Customer_Name, Contact_number
FROM CUSTOMER_DETAILS NATURAL JOIN CUSTOMER_ORDER NATURAL JOIN 
(ORDERS INNER JOIN TAXONOMY ON ORDERS.Plant_Name = TAXONOMY.Sci_Name) 
WHERE Com_Name="Mango";

/*3).The Management wants to plant plants which have been ordered by customers 
but have no record of arriving. 
Fetch the common names of all such plants.*/
SELECT DISTINCT Com_Name
FROM (TAXONOMY INNER JOIN ORDERS ON ORDERS.Plant_Name=TAXONOMY.Sci_Name) 
WHERE Sci_Name IN(
SELECT Plant_Name FROM ORDERS WHERE ORDERS.Plant_Name NOT IN (
SELECT Plant_Name FROM PENDING_ARRIVALS));

/*4). As a part of Business strategy, the management is interested to know the 
type of the top 2 most ordered plants.
Return the common names and the type of these 2 bestsellers.*/
SELECT DISTINCT Com_Name,Type_Name FROM TAXONOMY
NATURAL JOIN PLANT_DETAILS
NATURAL JOIN TYPE_AVAILABILITY
INNER JOIN (
    SELECT Plant_Name FROM ORDERS GROUP BY Plant_Name ORDER BY Count(*) DESC
    LIMIT 2) AS DETAILS 
WHERE TAXONOMY.Sci_Name=DETAILS.Plant_Name;

/* Aggregate Functions */
/*1).The Management wants to know the first names and the last names of the employees 
who perform more than 2 types of services. 
Print the first and last names of all those employees.*/
SELECT FName, Lname
FROM EMPLOYEE
WHERE EMPLOYEE.SSN IN(
    SELECT ESSN 
    FROM DUTY 
    GROUP BY ESSN 
    HAVING COUNT(*)>2);

/*2).The nursery wants a report on the number of plants in each aisle. Print the number of plants in each aisle.*/
SELECT COUNT(*), Plant_Aisle 
FROM PLANT
GROUP BY Plant_Aisle;

/*3).Print the revenue earned until the current date city-wise in descending order*/
SELECT SUM(PRICE), City 
FROM ORDERS 
GROUP BY City 
ORDER BY SUM(PRICE) DESC;

/*4).As a part of a school project, students are interested to know 
all the different Genera of plants that the nursery has. 
Display all the Genera and the number of species each holds.*/
SELECT DISTINCT SUBSTRING_INDEX(Sci_Name," ",1) AS GENERA, COUNT(*) AS SPECIES 
FROM TAXONOMY 
GROUP BY GENERA;

/* Set Operations */
/*1).Retrieve the names of the employees who are 
either heads at different locations 
or have been working for more than 3 years.*/
SELECT Fname,Lname
FROM EMPLOYEE
WHERE TIMESTAMPDIFF(YEAR,EMPLOYEE.Start_date,CURDATE())>3
UNION
SELECT Fname,Lname
FROM EMPLOYEE INNER JOIN LOCATION ON EMPLOYEE.SSN=LOCATION.Head_SSN;

/* 2).The management wants to increase the variety of plants it holds. 
Find the common names of all those plants 
whose information it has (Taxonomic data) but is not available (No plant as such in the nursery).*/
SELECT Com_Name
FROM TAXONOMY
EXCEPT
SELECT Com_Name 
FROM TAXONOMY NATURAL JOIN PLANT_DETAILS;

/*3).As an initiative to spread awareness about the many non-trivial benefits of plants, 
the management wants the common names of only those plants which are both Medicinal and Ornamental.*/
SELECT Com_Name
FROM TAXONOMY NATURAL JOIN PLANT_DETAILS NATURAL JOIN TYPE_AVAILABILITY 
WHERE Type_Name="Ornamental"
INTERSECT
SELECT Com_Name
FROM TAXONOMY NATURAL JOIN PLANT_DETAILS NATURAL JOIN TYPE_AVAILABILITY 
WHERE Type_Name="Medicinal";

/*4).The management is planning on reviewing the way Soil Conditioning is done at the Nurseries. 
However, to implement any changes, it needs to address the same to all the Heads at different locations. 
Retrieve the names and contact numbers of heads of all locations along with those 
who perform either composting or soil aeration.*/
SELECT Fname,Lname
FROM EMPLOYEE INNER JOIN LOCATION ON EMPLOYEE.SSN=LOCATION.Head_SSN 
UNION
SELECT Fname, Lname
FROM EMPLOYEE INNER JOIN DUTY ON EMPLOYEE.SSN=DUTY.ESSN 
WHERE Service="Soil Aeration" OR Service="Composting";

/*FUNCTIONS*/
/*The management is planning on increasing the salary of those employees who perform more than two duties. 
For such employees, a salary hike of 30% is expected. 
Write a function that implements the above expected salary without updating it.*/
DELIMITER $$
CREATE FUNCTION add_func_sal(a varchar(20)) RETURNS INT
BEGIN
DECLARE COUNT INT;
DECLARE SAL INT;
SET COUNT=(SELECT COUNT(*) FROM DUTY WHERE DUTY.ESSN=a GROUP BY ESSN); SET SAL=(SELECT SALARY FROM EMPLOYEE WHERE EMPLOYEE.SSN=a);
IF COUNT>2 THEN
SET SAL=SAL*1.3;
ELSE
SET SAL=SAL+0;
END IF;
RETURN SAL;
END $$
DELIMITER ;

/* Procedure */
/* As a way to recognise the efforts made by the Heads at different locations, 
the management has decided to increase the salary of the heads of the top location 
which has brought the most revenue, by 15%. 
However, it does not want the efforts of the other Location heads to go unnoticed, 
and hence decides to give the others a bonus of Rs.1000. Create a procedure that would implement the same 
at the end of the Nursery’s financial year i.e. 13th of November of this year.*/

DELIMITER $$
CREATE PROCEDURE Increase_Sal_Bonus()
BEGIN
DECLARE SSN_E varchar(20);
DECLARE CITY_MAX varchar(20);
SET CITY_Max=(SELECT City FROM ORDERS GROUP BY City ORDER BY SUM(PRICE) DESC LIMIT 1); SET SSN_E=(SELECT Head_SSN FROM LOCATION WHERE Location_name=CITY_MAX);
IF TIMESTAMPDIFF(DAY,"2022-11-13",CURDATE())=0 THEN
UPDATE EMPLOYEE
SET SALARY=SALARY*1.15
WHERE EMPLOYEE.SSN=SSN_E;
UPDATE EMPLOYEE
SET SALARY=SALARY+1000
WHERE EMPLOYEE.SSN!=SSN_E;
END IF;
END $$

DELIMITER ;

/* Triggers */
/* In order to ensure that no employee overworks himself/herself, 
the management has decided that no employee can take up more than 3 duties. 
Create a trigger that alerts the user if he/she tries to take up (insert) more than 3 services.*/
DELIMITER $$
CREATE TRIGGER Duties
BEFORE INSERT
ON DUTY FOR EACH ROW
BEGIN
DECLARE Count INT;
DECLARE Err_Mes varchar(100);
SET Count=(SELECT COUNT(*) FROM DUTY WHERE DUTY.ESSN=NEW.ESSN); SET Err_Mes="User cannot take any more services";
IF Count>3 THEN
SIGNAL SQLSTATE '45000'
SET MESSAGE_TEXT=Err_Mes;
END IF;
END $$

/* Cursor */
/* The management is curious to know the various tasks that are needed to maintain their nursery. 
Create a list that enumerates all such tasks using cursor and procedures.
*/

DELIMITER $$
CREATE PROCEDURE List_Tasks(INOUT list varchar(400))
BEGIN
DECLARE done INTEGER DEFAULT 0;
DECLARE task varchar(50) DEFAULT "";
DECLARE curs CURSOR FOR
SELECT DISTINCT Service FROM DUTY;
DECLARE CONTINUE HANDLER FOR NOT FOUND SET done=1; OPEN curs;
get_list: LOOP
FETCH curs into task;
IF done=1 THEN
LEAVE get_list;
END IF;
SET list=CONCAT(task,";",list);
END LOOP get_list;
CLOSE curs;
END $$
DELIMITER ;

