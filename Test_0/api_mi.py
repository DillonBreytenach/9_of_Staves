from crypt import methods
from flask import Flask, render_template, url_for
from main import main


#ToDo:
    #Login Page
    #Threading for connections
    #DashBoard
    #Game Table


app = Flask(__name__)
"""
class start:
    #Calls fuctions from seperate file
    def run():
        return None
"""        
@app.route('/home', methods=['GET', 'POST'])
def Home():
    #APP_HOME
    return render_template('home.html')

@app.route('/dashboard')
def Dashboard():
    #(PLAYER)SIGNED_IN_PAGE
    return render_template('dashboard.html')

@app.route('/login', methods=['GET', 'POST'])
def Login():
    #LOGIN_PAGE
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def Register():
    #LOGIN_PAGE
    return render_template('register.html')



if __name__ == '__main__':
    app.run(debug=True)