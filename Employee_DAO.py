import mysql.connector
import dbconfig as cfg

class EmployeesDAO:
    db=""
    def __init__(self):
        self.db = mysql.connector.connect(
            host = cfg.mysql['host'],
            user = cfg.mysql['user'],
            password = cfg.mysql['password'],
            database = cfg.mysql['database']
        )
        #print("connected")

    def create(self, employee):
        cursor = self.db.cursor()
        #sql command
        sql = "insert into employees (eid, fname, lname, gender, dcode, startdate) values (%s,%s,%s,%s,%s,%s)"
        # input values as dict object
        values = [ 
            employee['eid'],
            employee['fname'],
            employee['lname'],
            employee['gender'],
            employee['dcode'],
            employee['startdate']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

    # get all data
    def get_all(self):
        cursor=self.db.cursor()
        #sql command
        sql="select * from employees"
        cursor.execute(sql)
        results=cursor.fetchall()
        returnArray = []
        #print (results)
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)

        # return the array as dict object for sending to html
        return returnArray       

    def convertToDict(self,result):
        colnames=['eid','fname','lname','gender','dcode','startdate']
        employee ={}
        if result:
            for i, colName in enumerate (colnames):
                value = result[i]
                employee[colName] = value
        return employee

    # find by id
    def findById(self, eid):
        cursor=self.db.cursor()
        #command
        sql="select * from employees where eid = %s"
        values = [eid]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDict(result) 
    
    # update by eid
    def update(self, employee):
        cursor=self.db.cursor()
        sql="update employees set fname=%s, lname=%s, gender=%s, dcode=%s, startdate=%s where eid=%s"
        values = [
            employee['fname'],
            employee['lname'],
            employee['gender'],
            employee['dcode'],
            employee['startdate'],
            employee["eid"]
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return employee
    
    # delete by eid
    def delete(self, eid):
        cursor=self.db.cursor()
        sql="delete from employees where eid = %s"
        values = [eid]
        cursor.execute(sql, values)
        self.db.commit()
        return {}

employeeDAO = EmployeesDAO()
#one on the left not filename, but instance
#one on the right is the class name 