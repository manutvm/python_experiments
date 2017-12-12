import sqlite3


class Student:

    def __init__(self):
        self.connection = sqlite3.connect('/home/manu/My_Workspace/DemoProject/database/test.db')
        
        self.cursor = self.connection.cursor()
        
    def getStudentDetails(self):
        self.cursor.execute('''
        select id,name,marks from student
        ''')
        
        records = self.cursor.fetchall()
        
        records_list = []
        
        for record in records:
            record_list = [record[0], record[1], record[2]]
            records_list.append(record)            
            
        self.cursor.close()
        self.connection.close()
        
        return records_list
