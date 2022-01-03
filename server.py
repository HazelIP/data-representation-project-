# This is the server linking to DAO and html

from logging import info
from flask import Flask, json, jsonify,  request, redirect, url_for, abort, make_response, render_template, session
from Employee_DAO import employeeDAO

app = Flask(__name__,
            static_url_path='', 
            static_folder='static_page',
            )

app.secret_key = "data_rep"

@app.route('/')
# redirect to login if not logged in
def index():
    if not "Username" in session:
        return redirect (url_for('login'))
    
    return redirect (url_for('view'))

@app.route('/login', methods=['GET','POST'])
# login page, redirect to view employee if credentials matched
def login():
    error = None
    if request.method == 'POST':
        session['username'] = request.form['Username']
        session['password'] = request.form['Password']
        # if credential not matched, give feedback and link to login again
        if session['username'] != 'abc@gmail.com' or session['password'] != '123456':
            return "Invalid Credentials. Use the ones provided <br><a href='/login'>" + "click here to try again</a>" 
        else:
            return redirect (url_for('view'))
    return render_template("login.html", error=error)

@app.route('/logout')
# clear the session and redirect to login again after logout button is clicked
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/view')
def view():
    # cannot view unless logged in
    if not 'username' in session:
        abort(401)
    return render_template("view.html")

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
