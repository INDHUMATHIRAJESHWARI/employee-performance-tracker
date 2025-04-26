import pymysql
import csv

class Employee:
    def __init__(self):
        self.connection = pymysql.connect(
        host='localhost',
        user='root',
        password='Indhu',
        database='employee_performance'
        )

    def insert_employee(self,name,age,dept,position,hire_date):
        cursor =self.connection.cursor()
        cursor.execute("""
        INSERT INTO employees(name,age,department,position,hire_date) VALUES (%s, %s, %s, %s, %s)""",(name,age,dept,position,hire_date))
        self.connection.commit()
        cursor.close()

    def update_employee(self,name,age,dept,position,hire_date,employee_id):
        cursor =self.connection.cursor()
        cursor.execute("""UPDATE employees SET name = %s, age = %s, department = %s, position = %s, hire_date = %s WHERE employee_id = %s""",
                       (name,age,dept,position,hire_date,employee_id))
        self.connection.commit()
        cursor.close()

    def delete_employee(self,employee_id):
        cursor = self.connection.cursor()
        cursor.execute("""DELETE FROM employees WHERE employee_id = %s""",(employee_id))
        self.connection.commit()
        cursor.close()

    def get_employee_by_id(self,employee_id):
        cursor =self.connection.cursor()
        cursor.execute("""SELECT * FROM employees WHERE employee_id = %s""",(employee_id))
        res=cursor.fetchall()
        for row in res:
            print(f"Employee ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Department: {row[3]}, Position: {row[4]}, Hire Date: {row[5]}")       
        cursor.close()

    def get_employee(self):
        cursor = self.connection.cursor()
        cursor.execute("""SELECT * FROM employees""")
        res=cursor.fetchall()
        for row in res:
            print(row)
        cursor.close()
        
    def export_to_csv(self,fname):
        cursor=self.connection.cursor()
        cursor.execute("""SELECT * FROM employees""")
        res=cursor.fetchall()
        field=['employee_id', ' name   ','age',' department ','position  ',' hire_date']
        with open (fname,mode='w',newline='') as f:
            file=csv.writer(f)
            file.writerow(field)
            for row in res:
                file.writerow(row)
            print(f"Imported succesfully from db table to {fname} file!")
        cursor.close()

    def cancel(self):
        self.connection.close()
        print("App closed!")