
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
    def create(self,person):
        cursor=self.db.cursor()
        #do insert
        sql="insert into employees (id, name) values (%s, %s)"
        values = [
            person["id"],
            person['name']
        ]
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
        colnames=['id','name']
        person ={}

        if result:
            for i, colname in result:
                value = result[i]
                person[colname]
        return person

    # get by id
    # update
    # delete
employeesDAO = EmployeesDAO()
