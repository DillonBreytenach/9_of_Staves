from crypt import methods
from flask import Flask
from main import main



app = Flask(__name__)
class start:
    def run():
        main.greet()

@app.route('/', methods=['GET', 'POST'])
def great():
    return start.run()

if __name__ == '__main__':
    app.run(debug=True)