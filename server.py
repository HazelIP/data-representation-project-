# This is the server
#!flask/bin/python

from flask import Flask, jsonify,  request, abort, make_response

from Employee_DAO import EmployeesDAO

app = Flask(__name__,
            static_url_path='', 
            static_folder='../')

# get all
@app.route('/')
# login page?
def index():
    return "Hello!"

# CRUD
@app.route('/employee')
def get_all():
    return "served by get all()"

@app.route('/employee/<int:id>')
def get_by_id():
    return "served by get by id"

@app.route('/employee', methods=['POST'])
def create():
   
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
    return jsonify(EmployeesDAO.create(employee))

    return "served by Create "

#update
# curl -X PUT -d "{\"Title\":\"new Title\", \"Price\":999}" -H "content-type:application/json" http://127.0.0.1:5000/books/1


@app.route('/employee/<int:eid>', methods=['PUT'])
def update(eid):
    foundEmployee=EmployeesDAO.findById(eid)
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
    EmployeesDAO.update(currentEmployee)

    return jsonify(currentEmployee)

#delete
# curl -X DELETE http://127.0.0.1:5000/books/1


@app.route('/employee/<int:eid>', methods=['DELETE'])
def delete(eid):
    EmployeesDAO.delete(eid)

    return jsonify({"done": True})


if __name__ == "__main__":
    app.run(debug=True)














if __name__ == '__main__' :
    app.run(debug= True)   