import os
import yaml
from flask import Flask, request, jsonify
from flask_cors import CORS

from _helpers import db

manager = db.manager()

app = Flask(__name__)
CORS(app)

@app.route('/health-check', methods=["GET"])
def ping():
    return "ok"

@app.route(f'/', methods=["GET"])
def log():
    return jsonify({"logs": manager.get_structure()})

@app.route(f'/log/<name>', methods=["GET"])
def log_name(name): 
    return jsonify({"logs": manager.get_log(name)})

@app.route(f'/add_log/<name>', methods=["GET"])
def add_log(name):
    if 'data' in request.args:
        if manager.add_log(name, request.args.get("data")):
            return jsonify({"status": "ok"})
        else:
            return jsonify({"status": "error"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 8082))