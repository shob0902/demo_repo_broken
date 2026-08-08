"""Toy Flask app used as the end-to-end demo target for the agent swarm.

/signup currently accepts any payload with no validation -- that's the bug
the demo task asks the swarm to fix (see README.md in this folder).
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

users = []


@app.route("/signup", methods=["POST"])
def signup():
    data = request.get_json(force=True, silent=True) or {}
    email = data.get("email", "")
    password = data.get("password", "")

    users.append({"email": email, "password": password})
    return jsonify({"status": "ok", "email": email}), 201


if __name__ == "__main__":
    app.run(debug=True)
