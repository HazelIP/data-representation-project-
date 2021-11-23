
import mysql.connector 
    #should go into config file
    '''mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="hazel",
        database="employees2"'''

class EmployeesDAO:
    db=""
    def__init__(self):
        self.db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="hazel",
        database="employees2"    
    )
    def create(self,values):
        cursor=self.db.cursor()
        #do insert
        sql="insert into employees (id, name) values (%d, %s)"
        values = (1, john)
        cursor.execute(sql, values)

        self.db.commit()
        return cursor.lastrowid

    # get data
    def get_all(self):
        cursor=self.db.cursor()
        #command
        sql="select * from employees"
        cursor.execute(sql)
        result=cursor.fetchall()
        for x in result:
            print(x) #need to jsonify it

    # get by id
    # update
    # delete
employeesDAO = EmployeesDAO()
