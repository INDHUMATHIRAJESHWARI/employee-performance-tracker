import pymysql

class performance_view:
    def __init__(self):
       self.Connection = pymysql.connect(
        host='localhost',
        user='root',
        password='Indhu',
        database='employee_performance'
        )
       
    def save_review(self,employee_id, score, feedback):
        cursor = self.Connection.cursor()
        cursor.execute('''
        INSERT INTO performance_reviews (employee_id, review_date, score, feedback)
        VALUES (%s, CURDATE(), %s, %s)
        ''', (employee_id, score,feedback))
        self.Connection.commit()
        cursor.close()
    
    def get_review(self):
        cursor=self.Connection.cursor()
        cursor.execute("""
        SELECT * FROM performance_reviews
        """)
        res=cursor.fetchall()
        for row in res:
            print(f"Review ID: {row[0]}, Employee ID: {row[1]}, Review date: {row[2]} , Score: {row[3]}, Feedback: {row[4]}")
        cursor.close()


    def get_top_performers(self):
        cursor = self.Connection.cursor()
        cursor.execute('SELECT * FROM top_performers')
        top_performers = cursor.fetchall()
        for row in top_performers:
            print(f"Name: {row[0]}, Department: {row[1]}, Average Score: {row[2]}")
        cursor.close()

    def get_review_audit(self):
        cursor = self.Connection.cursor() 
        res=cursor.execute("""SELECT * FROM audit_log""")
        """for row in res:
            print(f"log ID:{row[0]},action: {row[1]},timestamp:{row[2]}")"""
        cursor.close()