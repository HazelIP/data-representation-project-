# This is the server linking to DAO

from flask import Flask, json, jsonify,  request, redirect, url_for, abort, make_response, render_template
from Employee_DAO import employeeDAO

app = Flask(__name__,
            static_url_path='', 
            static_folder='static_page',
            )

@app.route('/')
# redirect to login at index
def index():
    return redirect (url_for('login'))
    #return "hello"

@app.route('/login')
def login():
    return render_template("login.html")


# CRUD - get all
# curl http://127.0.0.1:5000/employee
@app.route('/employee')
def get_all():
    return jsonify(employeeDAO.get_all()) 
    #return "served by get all()"

# find by eid
# curl http://127.0.0.1:5000/employee/1234
@app.route('/employee/<int:eid>')
def find_by_id(eid):
    return jsonify(employeeDAO.findById(eid))
# catch error if eid not found?

#create new employee
#curl -X POST -d "{\"eid\":\"1233\", \"fname\":\"Mary\",\"lname\":\"Doe\",\"gender\":\"F\",\"dcode\":\"101S\",\"startdate\":\"2020-01-01\"}" -H Content-Type:application/json http://127.0.0.1:5000/employee
@app.route('/employee', methods=['POST'])
def create():
    if not request.json:
        abort(400)
    employee = {
        "eid": request.json["eid"],
        "fname": request.json["fname"],
        "lname": request.json["lname"],
        "gender": request.json["gender"],
        "dcode": request.json["dcode"],
        "startdate": request.json["startdate"]
    }
    return jsonify(employeeDAO.create(employee))

#update existing employee
# curl -X PUT -d "{\"fname\":\"Mary\",\"lname\":\"Doe\",\"gender\":\"F\",\"dcode\":\"101S\"}" -H Content-Type:application/json http://127.0.0.1:5000/employee/1234
@app.route('/employee/<int:eid>', methods=['PUT'])
def update(eid):
    foundEmployee=employeeDAO.findById(eid)
    #print (foundEmployee)
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
#curl -X DELETE http://127.0.0.1:5000/employee/1234
@app.route('/employee/<int:eid>', methods=['DELETE'])
def delete(eid):
    employeeDAO.delete(eid)
    return jsonify({"done": True})


if __name__ == "__main__":
    app.run(debug=True)
