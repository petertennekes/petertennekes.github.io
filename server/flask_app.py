
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask_cors import cross_origin
from server import get_open_graph
app = Flask(__name__)

@app.route('/')
@cross_origin()
def hello_world():
    return get_open_graph()

