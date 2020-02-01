from flask import Flask, request, abort, render_template, send_from_directory
from students import get_students
import json


app = Flask(__name__)


@app.route('/students', methods=['GET'])
def local_endpoint():
    return get_students()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

