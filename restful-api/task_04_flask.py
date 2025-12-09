#!/usr/bin/python3
"""This is just a doc"""


from flask import Flask, jsonify, request


app = Flask(__name__)

'''users = {"jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"}, "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}}'''
users = dict()

@app.route('/')
def home():
    return 'Welcome to the Flask API!'

@app.route('/data')
def data():
    userslist = list(users.keys())
    print(userslist)
    return jsonify(userslist)

@app.route('/status')
def status():
    return 'OK'

@app.route('/users/<username>')
def finduser(username):
    if users.get(username):
        return jsonify(users.get(username))
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    global users
    try:
        data = request.get_json(force=True)
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400
    un = data.get('username')
    if not un:
        return jsonify({"error": "Username is required"}), 400
    elif un in users:
        return jsonify({"error": "Username already exists"}), 409
    name = data.get('name')
    age = data.get('age')
    city = data.get('city')
    users[un] = {'username': un, 'name': name, 'age': age, 'city': city}
    confmes = {'message': 'User added', 'user': users[un]}
    return jsonify(confmes), 201

if __name__ == '__main__':
    app.run()
