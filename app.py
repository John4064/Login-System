from flask import Flask, redirect, url_for, request, render_template


app = Flask(__name__)

@app.route('/')
def home():  # put application's code here
    return render_template('templates/home.html')

@app.route('/user/<name>')
def userpage(name):  # put application's code here
    return render_template('templates/userpage.html', title=str(name))


#Catch all extra routes
@app.route('/', defaults={'u_path': ''})
@app.route('/<u_path>')
def catch_all(u_path):
    print(repr(u_path))
    return render_template("templates/dead.html")

if __name__ == '__main__':
    app.run()
