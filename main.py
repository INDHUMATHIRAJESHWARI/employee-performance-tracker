import employee
import performance

try:
    employee_db=employee.Employee()

    performance_db=performance.performance_view()

    while True:
        print("\n\n Dashboard")
        print("1. Add Employee\n2. Update Employee\n3. Delete Employee\n4. Get Employee by ID\n5. Get All Employees\n6. Add Performance Review\n7. Get all reviews\n8. Get Top Performers\n9. Export as CSV\n10. View review audit\n0. Exit")
        
        ch=int(input("Enter your choice(0-10) : "))

        if ch == 1:
            print("\nAdd Employee details")
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            dept = input("Enter department: ")
            position = input("Enter position: ")
            hire_date = input("Enter hire date (YYYY-MM-DD): ")
            employee_db.insert_employee(name, age, dept, position, hire_date)
        elif ch == 2:
            print("\nUpdate Employee details")
            employee_id = int(input("Enter employee ID to update: "))
            name = input("Enter new name: ")
            age = int(input("Enter new age: "))
            dept = input("Enter new department: ")
            position = input("Enter new position: ")
            hire_date = input("Enter new hire date (YYYY-MM-DD): ")
            employee_db.update_employee(name, age, dept, position, hire_date,employee_id)
        elif ch == 3:
            print("\nDeleted Employee details")
            employee_id = int(input("Enter employee ID to delete: "))
            employee_db.delete_employee(employee_id)
        elif ch == 4:
            print("\nEmployee by ID")
            employee_id = int(input("Enter employee ID: "))
            employee_db.get_employee_by_id(employee_id)
        elif ch == 5:
            print("\nAll Employees")
            employee_db.get_employee()
        elif ch == 6:
            print("\nAdd Performance Review")
            employee_id = int(input("Enter employee ID: "))
            score = int(input("Enter performance score (1-10): "))
            feedback = input("Enter feedback: ")
            performance_db.save_review(employee_id, score, feedback)
        elif ch == 7:
            print("\n All performance Reviews")
            performance_db.get_review()
        elif ch == 8:
            print("\n Get Top Performers")
            performance_db.get_top_performers()
        elif ch == 9:
            fname=input("\n Enter file name : ")
            print("\n CSV file of employee DB")
            employee_db.export_to_csv(fname)
        elif ch == 10:
            print("\n Review Audit log")
            performance_db.get_review_audit()
        elif ch == 0:
            employee_db.cancel()
            break

except Exception as e:
    print(f"error ~ {e}")