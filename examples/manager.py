from flask import Flask
from flask.ext.runner import Manager 

app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def index():
    return "Hello, world!"

if __name__ == '__main__':
    manager.run()

