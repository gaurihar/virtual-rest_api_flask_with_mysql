#from flask import Flask
#app = Flask(__name__)
#app.run()
from api.user import app

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=4300)