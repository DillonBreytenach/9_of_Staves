from crypt import methods
from flask import Flask
from main import main

#ToDo:
    #Threading 


app = Flask(__name__)
class start:
    #Calls fuctions from seperate file
    def run():
        return main.greet()

@app.route('/', methods=['GET', 'POST'])
def great():
    #APP_
    return start.run()

if __name__ == '__main__':
    app.run(debug=True)