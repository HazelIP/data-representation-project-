from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def login():
    return "in login"
    # to render another login.html file
    #return render_temaplate("login.html")





if __name__ == '__main__':
    app.run(debug=True)