# This is the server
#!flask/bin/python

from flask import Flask, json, jsonify,  request, redirect, url_for, abort, make_response

from Employee_DAO import employeeDAO

app = Flask(__name__,
            static_url_path='', 
            static_folder='../')

# hard-code some data to test




# get all
@app.route('/')
# login page?
def index():
    return redirect (url_for('login'))
    #return "Hello!"

@app.route('/login')
def login():
    #return "served by login"
    abort(401)
    #this_is_never_executed() #function not defined


# CRUD - get all
@app.route('/employee')
def get_all():
    return jsonify(employee) #display the data, where's the data?
    return "served by get all()"

# find by eid
@app.route('/employee/<int:eid>')
def get_by_id(id):
    foundEmployee = list(filter(lambda t:t["eid"]== id,employee))
    if len(foundEmployee) == 0:
        return jsonify({}), 204
    return jsonify(foundEmployee[0])
    #return "served by get by id"

#create new employee
@app.route('/employee', methods=['POST'])
def create():
    #global nextId
    if not request.json:
        abort(400)
## change these
    employee = {
        "eid": request.json["eid"],
        "fname": request.json["fname"],
        "lname": request.json["lname"],
        "gender": request.json["gender"],
        "dcode": request.json["dcode"],
        "startdate": request.json["startdate"]
    }
    employee.append(employee)
    return jsonify(employeeDAO.create(employee))

    return "served by Create "

#update existing employee
# curl -X PUT -d "{\"Title\":\"new Title\", \"Price\":999}" -H "content-type:application/json" http://127.0.0.1:5000/books/1

@app.route('/employee/<int:eid>', methods=['PUT'])
def update(eid):
    foundEmployee=employeeDAO.findById(eid)
    print (foundEmployee)
    if foundEmployee == {}:
        return jsonify({}), 404
    currentEmployee = foundEmployee
    if 'fname' in request.json:
        currentEmployee['fname'] = request.json['fname']
    if 'lname' in request.json:
        currentEmployee['lname'] = request.json['lname']
    if 'gender' in request.json:
        currentEmployee['gender'] = request.json['gender']
    if 'dcode' in request.json:
        currentEmployee['dcode'] = request.json['dcode']
    if 'startdate' in request.json:
        currentEmployee['startdate'] = request.json['startdate']
    employeeDAO.update(currentEmployee)

    return jsonify(currentEmployee)

#delete existing employee
# curl -X DELETE http://127.0.0.1:5000/books/1

@app.route('/employee/<int:eid>', methods=['DELETE'])
def delete(eid):
    employeeDAO.delete(eid)

    return jsonify({"done": True})


if __name__ == "__main__":
    app.run(debug=True)














if __name__ == '__main__' :
    app.run(debug= True)   