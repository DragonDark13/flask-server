from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins="*")  # This will enable CORS for all routes


@app.route('/members')
def members():
    members_list = ["Member1", "Member2", "Member3"]
    return jsonify({"members": members_list})


@app.route("/api/users", methods=['GET'])
def get_users():
    users_list = ["User1", "User2", "User3"]
    return jsonify({"users": users_list})


if __name__ == "__main__":
    app.run(debug=True, port=8080)
