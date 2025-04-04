from flask import Flask, session, request, jsonify
from flask_cors import CORS
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "super_secret_key"  # Change this in production

# Session config
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)

# Enable CORS with credentials
CORS(app, supports_credentials=True)

@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    session["user"] = username
    return jsonify({"message": f"Logged in as {username}"}), 200

@app.route("/api/logout", methods=["POST"])
def logout():
    session.pop("user", None)
    return jsonify({"message": "Logged out"}), 200

@app.route("/api/me", methods=["GET"])
def me():
    user = session.get("user")
    if user:
        return jsonify({"user": user}), 200
    return jsonify({"error": "Not logged in"}), 401

if __name__ == "__main__":
    app.run(debug=True)