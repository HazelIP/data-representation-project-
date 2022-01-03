# Employee Restful API
 A Data Representation Project

This program has a Flask server that consume Restful API and links to a sql database `employees`. User is redirected to login page at index, after matching credentials, user will be redirected to a webpage to view employee and perform CRUD operation to the databses. 

The server links to a file `Employee_DAO` which links to the SQL database 

# Install
- Make sure to check the `requirements.txt` and have the packages installed. 

# Run
After pulling the repository from gitHub, open cmder, move to the directory where the repository is store. 
1. Activate virtual environment
2. Run the program `server.py`
3. Copy the link where the server is run on and open it on browser
4. Log-in using Email `abc@gmail.com` and password `123456`
5. User will be redirected to `view.html`
6. Perform CRUD operation through the web interface
7. Click log out button and will be redirected to step 4.
