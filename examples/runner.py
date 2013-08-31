from flask import Flask
from flask.ext.runner import Runner 

app = Flask(__name__)
runner = Runner(app)

@app.route('/')
def index():
    return "Hello, world!"

if __name__ == '__main__':
    runner.run()

