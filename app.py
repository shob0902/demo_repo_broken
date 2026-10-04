"""Toy Flask app used as the end-to-end demo target for the agent swarm.

/signup currently accepts any payload with no validation -- that's the bug
the demo task asks the swarm to fix (see README.md in this folder).
"""
import re
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Simple email regex pattern for basic validation
EMAIL_REGEX = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

users = []


@app.route("/signup", methods=["POST"])
def signup():
    data = request.get_json(force=True, silent=True) or {}
    email = data.get("email", "")
    password = data.get("password", "")

    # Validate email format
    if not EMAIL_REGEX.match(email):
        abort(400, description="Invalid email format")
    # Validate password presence
    if not password:
        abort(400, description="Password is required")

    users.append({"email": email, "password": password})
    return jsonify({"status": "ok", "email": email}), 201


if __name__ == "__main__":
    app.run(debug=True)
