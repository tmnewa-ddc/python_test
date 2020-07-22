import os

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/cpu', methods=['GET'])
def cpus():
    return jsonify({'cpus': os.cpu_count()})
