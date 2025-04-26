## Employee performance Tracker
   A python application to manage employee records and performance reviews using PyMySQL to interact with MySQL Database.  

## Features
   --> Add, Update, Delete employee records 
   --> View employee details by specific id or overall
   --> Export data as CSV file whenever required
   --> Add performance reviews in scores(1-10) or as text
   --> View all reviews
   --> Get good performing employees
   --> Auidt logging
   --> Views for reporting
   --> Ensured data integrity using constraints.

## Tech stack
   --> Python 3.x
   --> PyMySQL (MySQL Connector)
   -->MySQL DB

## DB 
   --> CREATE DATABASE employee_performance;
   --> pip install pymysql
   --> pyhton database.py (initialize DB)

## Usage
   --> python main.py
   --> Following menu prompts
         1.Add Employee
         2.Update Employee
         3.Delete Employee
         4.Get Employee by ID
         5.Get All Employees
         6.Add Performance Review
         7.Get all reviews
         8.Get Top Performers
         9.Export as CSV
         10.View review audit
         0.Exit

## Future Enhancements
   --> User authentication
   --> Input validation etc..,