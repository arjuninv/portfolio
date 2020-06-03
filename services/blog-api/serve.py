from flask import Flask, request, jsonify
import jwt

app = Flask(__name__)

@app.route('/ping', methods=["GET"])
def ping():
    return "ok"


@app.route('/auth', methods=["POST"])
def auth():
    data=request.json
    if data['type'] == "create_account":
        if all([x in data for x in ['username', 'password', 'email']]):
            encode_data = {
                'username': data['username'], 
                'email': data['email']
                }
            try:
                access_token = jwt.encode(encode_data,'secret', algorithm='HS256')
                return jsonify(
                    {"status": "ok",
                    "access_token": access_token})
            except:
                return jsonify({"status": "error"})
        else:
            return jsonify({"status": "error"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8081)