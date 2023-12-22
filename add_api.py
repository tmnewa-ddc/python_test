import os

from flask import Flask, jsonify, request, make_response

app = Flask(__name__)


@app.route('/add', methods=['GET'])
def add():
    login = request.args.get('login')
    if login == "true":
        a = request.args.get('a')
        b = request.args.get('b')
        if a is not None:
            if b is not None:
                a, b = int(a), int(b)
                return make_response(jsonify({"sum": a + b}), 200)
            else:
                return make_response(jsonify(), 400)
        else:
            return make_response(jsonify(), 400)
    else:
        return make_response(jsonify(), 401)





















# 請假裝看不到
# def ___():
#     login = request.args.get('login')
#     if login != "true":
#         return make_response(jsonify(), 401)
#
#     a = request.args.get('a')
#     b = request.args.get('b')
#
#     if a is None or b is None:
#         return make_response(jsonify(), 400)
#
#     a, b = int(a), int(b)
#     return make_response(jsonify({"sum": a + b}), 200)
