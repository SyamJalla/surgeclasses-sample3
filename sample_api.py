from flask_cors import CORS
from flask import Flask, jsonify, request

import argparse
import json
import ast
import os


app = Flask(__name__)
cors = CORS(app)


@app.route('/get_definations', methods=['POST', 'GET'])
def get_definations():
    data = request.args
    data.to_dict(flat=False)
    category = data['category'].lower()

    msg_dict = [{"Text": category}]

    return jsonify({"msg_dict": msg_dict})


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', type=int, help='Port Number', default=5051)
    parser.add_argument('--host', type=str, help='Host', default='0.0.0.0')
    args = parser.parse_args()

    host = args.host
    port = args.port

    app.run(host='0.0.0.0', port=5051, debug=False)
