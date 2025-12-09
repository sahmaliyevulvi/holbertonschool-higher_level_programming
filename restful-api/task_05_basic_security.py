#!/usr/bin/env python3
""" Authenticating system with flask """
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, get_jwt, create_access_token, jwt_required, get_jwt_identity
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "soSecret"

#-------------------------------
# We can also manage the errors
# like token is invalid or need a refresh
#------------------------------------

jwt = JWTManager(app)

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401

users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

#-------------------------------------
#    The basic form of the authentication is
#    username and password each time a request made
#-----------------------------------------

auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users[username]["password"], password):
                return users[username]
    return None

@app.route("/basic-protected")
@auth.login_required
def prot_bas():
    return "Basic Auth: Access Granted"

#----------------------------------------------
# Or we can just use the username and
# the password only in the login section
# And create a token to check the auth session
#-----------------------------------------------

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data["username"]
    password = data["password"]

    if username not in users.keys():
        return jsonify({"msg":"User not found!"}), 404

    if not check_password_hash(users[username].get("password"), password):
        return jsonify({"msg":"Invalid user credentials"}), 401

    token = create_access_token(identity=username, additional_claims={"role": users[username].get("role")})

    return jsonify({"access_token": token})

@app.route("/jwt-protected")
@jwt_required()
def prot_jwt():
    return "JWT Auth: Access Granted"

@app.route("/admin-only")
@jwt_required()
def admin_page():
    user = get_jwt()
    role = user.get("role")

    if role != "admin":
        return jsonify({"error":"Admin access required"}), 403
    return "Admin Access: Granted"

if __name__ == "__main__": app.run()
