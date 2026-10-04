"""Toy Flask app used as the end-to-end demo target for the agent swarm.

/signup currently accepts any payload with no validation -- that's the bug
the demo task asks the swarm to fix (see README.md in this folder).
"""
from flask import Flask, jsonify, request
import re

app = Flask(__name__)

users = []


@app.route("/signup", methods=["POST"])
def signup():
    data = request.get_json(force=True, silent=True) or {}
    email = data.get("email", "")
    password = data.get("password", "")

        # Validate email format
    email_regex = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
    if not re.match(email_regex, email):
        return jsonify({"error": "Invalid email format"}), 400
    # Validate password presence
    if not password:
        return jsonify({"error": "Password is required"}), 400

    users.append({"email": email, "password": password})
    return jsonify({"status": "ok", "email": email}), 201


if __name__ == "__main__":
    app.run(debug=True)
