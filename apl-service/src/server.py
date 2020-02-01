from flask import Flask, request, abort, render_template, send_from_directory
from results import get_results
import os

API_URI = 'http://' + os.environ['BACKEND_HOST'] +':' + os.environ['BACKEND_PORT'] + '/students'

app = Flask(__name__)


@app.route('/results', methods=['GET'])
def local_endpoint():
    return get_results(API_URI)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)

