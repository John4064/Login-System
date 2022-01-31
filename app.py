from flask import Flask, redirect, url_for, request, render_template
from config import *

app = Flask(__name__)

@app.route('/')
def home():  # put application's code here
    return render_template('home.html')

@app.route('/login')
def loginsystem():
    return render_template("login.html")

#figure this oput
@app.route('/handle_data', methods=['POST'])
def handle_data():
    projectpath = request.form['projectFilepath']
    # your code
    # return a response


"""
@app.route('/user/<name>')
def userpage(name):  # put application's code here
    return render_template('profile.html', title=str(name))
"""

#Catch all extra routes
@app.route('/', defaults={'u_path': ''})
@app.route('/<u_path>')
def catch_all(u_path):
    print(repr(u_path))
    return render_template("dead.html")

if __name__ == '__main__':
    app.run()
