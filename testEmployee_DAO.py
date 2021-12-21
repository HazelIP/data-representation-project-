from Employee_DAO import employeeDAO
from server import get_by_id
# from the file import the instance

employee1 = {
    "eid":1234,
    "fname":"John",
    "lname":"Doe",
    "gender":"M",
    "dcode":"101S",
    "startdate":"2020-01-01"
}
employee2 = {
    "eid":1235,
    "fname":"Susan",
    "lname":"Doe",
    "gender":"F",
    "dcode":"101S",
    "startdate":"2020-01-02"
}

# these go into server.py
#returnValue = employeeDAO.create(employee1)
#print(returnValue)
returnValue = employeeDAO.get_all()
print("get all")
print(returnValue)
returnValue = employeeDAO.findById(employee1['eid'])
print("find by id")
print(returnValue)
returnValue = employeeDAO.update(employee2)
print("update")
print(returnValue)
returnValue = employeeDAO.delete(employee2['eid'])
print("delete")
print(returnValue)