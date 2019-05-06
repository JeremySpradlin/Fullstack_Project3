#Testing demo server from flask and WSGI tutorial
from flask import Flask
app = Flask(__name__)
@app.route(/)
def hello():
    return "Hello, Flask!"

if __name__ == "__main__":
    app.run()