from Employee_DAO import employeeDAO
# from the file import the instance

employee = {
    "eid":1234,
    "fname":"John",
    "lname":"Doe",
    "gender":"M",
    "dcode":"101S",
    "startdate":"2020-01-01"
}

#EmployeesDAO.create(employee)
returnValue=employeeDAO.create(employee)
print(returnValue)