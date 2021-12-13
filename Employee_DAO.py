import mysql.connector

    #should go into config file
'''mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="data_representation"'''

class EmployeesDAO:
    db=""
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="data_representation"    
        )
        #print("connected")

    def create(self, employee):
        cursor = self.db.cursor()
        sql = "insert into employees (eid, fname, lname, gender, dcode, startdate) values (%s, %s, %s, %s, %s, %s)"
        values = {
            employee['eid'],
            employee['fname'],
            employee['lname'],
            employee['gender'],
            employee['dcode'],
            employee['startdate']
        }
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

    # get data
    def get_all(self):
        cursor=self.db.cursor()
        #command
        sql="select * from employees"
        cursor.execute(sql)
        results=cursor.fetchall()
        returnArray = []
        print (results)
        for result in results:
            returnAsDict = self.convertToDict(result)
            returnArray.append(returnAsDict)
        return returnArray       

    def converToDict(self,result):
        colnames=['eid','fname','lname','gender','dcode','startdate']
        employee ={}
        if result:
            for i, colname in result:
                value = result[i]
                employee[colname]
        return employee

    # get by id, not done
    def get_by_eid(self):
        cursor=self.db.cursor()
        #command
        sql="select * from employees where eid ="
        cursor.execute(sql)
        results=cursor.fetchone()
        returnArray = []
        print (results)
        for result in results:
            returnAsDict = self.convertToDict(result)
            returnArray.append(returnAsDict)
        return returnArray 
    
    # update, not done
    def update(self, employee):
        cursor=self.db.cursor()
        sql="insert into employees (eid, fname, lname, gender, dcode, startdate) values (%s, %s, %s, %s, %s, %s)"
        values = [
            employee["eid"],
            employee['fname'],
            employee['lname'],
            employee['gender'],
            employee['dcode'],
            employee['startdate']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid
    
    # delete, not done
    def delete(self, employee):
        cursor=self.db.cursor()
        sql="insert into employees (eid, fname, lname, gender, dcode, startdate) values (%s, %s, %s, %s, %s, %s)"
        values = [
            employee["eid"],
            employee['fname'],
            employee['lname'],
            employee['gender'],
            employee['dcode'],
            employee['startdate']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

#one on the left not filename, but instance
#one on the right is the class name 
employeeDAO = EmployeesDAO()
