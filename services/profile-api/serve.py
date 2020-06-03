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
def profile():
    structure = yaml.safe_load(manager.get_structure()) 
    return jsonify(structure)

@app.route(f'/page/<page>', methods=["GET"])
def profile_page(page):
    page_data = yaml.safe_load(manager.get_page(page)) 
    return jsonify(page_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 8081))