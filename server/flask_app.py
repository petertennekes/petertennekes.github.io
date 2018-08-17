
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask_cors import cross_origin
from open_graph import get_open_graph
from flask import request
from werkzeug.contrib.cache import FileSystemCache

app = Flask(__name__)
cache = FileSystemCache('/var/tmp/OpenGraphhCahche')
@app.route('/')
@cross_origin()
def hello_world():
    url = request.args.get('url')
    if url:
        response = cache.get(url)
        if response is None:
            response = get_open_graph(url)
            cache.set(url, response, timeout=60*60)
        return response
    else:
        return "error"

