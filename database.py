import pymysql

def DB_Setup():
    # Connect to the database
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='Indhu',
        database='employee_performance'
    )

    cursor = connection.cursor()

    try:
        # Create the employee table
        cursor.execute("""
            CREATE TABLE employees (
                employee_id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(50) NOT NULL,
                age INT NOT NULL,
                department VARCHAR(20) NOT NULL,
                position VARCHAR(20) NOT NULL,
                hire_date DATE NOT NULL
            )""")
        
        # Create performance table
        cursor.execute("""
            CREATE TABLE performance_reviews(
                review_id INT AUTO_INCREMENT PRIMARY KEY,
                employee_id INT,
                review_date DATE,
                score INT CHECK (score BETWEEN 1 AND 10),
                feedback TEXT,
                FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
            )""")
        
        # Create audit log table
        cursor.execute("""
            CREATE TABLE audit_log (
                log_id INT AUTO_INCREMENT PRIMARY KEY,
                action VARCHAR(50),
                timestamp DATETIME
            )""")
        
        # trigger creation 
        #cursor.execute(""" DROP TRIGGER IF EXISTS log_new_review""")
        
        cursor.execute("""
            CREATE TRIGGER log_new_review
            AFTER INSERT ON performance_reviews
            FOR EACH ROW
            INSERT INTO audit_log (action, timestamp)
            VALUES ('New review added', NOW())
        """)
        
        # Create view for top performers 
        cursor.execute("""
            CREATE VIEW top_performers AS
                SELECT e.name, e.department, AVG(p.score) as avg_score
                FROM employees e
                JOIN performance_reviews p ON e.employee_id = p.employee_id
                GROUP BY e.employee_id
                HAVING AVG(p.score) >= 8
            """)
        
        connection.commit()
        print("Database setup completed successfully!")
        
    except pymysql.Error as e:
        print(f"Error setting up database: {e}")
        connection.rollback()
    finally:
        connection.close()

DB_Setup()