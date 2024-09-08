from flask import Flask, jsonify, request
from flask_cors import CORS
import webbrowser
import validations

users_db = [
    {
        "id": 1,
        "password": 'abc1234',
        "name": 'juan',
        "lastname": 'perez'
    },
    {
        "id": 2,
        "password": 'abc1234',
        "name": 'pedro',
        "lastname": 'rodriguez'
    },
    {
        "id": 3,
        "password": 'abc1234',
        "name": 'carlos',
        "lastname": 'juarez'
    },
]

app = Flask(__name__)
CORS(app)

@app.get('/api/v1/users')
def get_users():
    return jsonify(users_db)

@app.get('/api/v1/user')
def get_user():
    user_id = request.args.get('user_id')

    valid_user_id = validations.validate_positive_integer(user_id)

    if not valid_user_id[0]:
        return jsonify({
            "name": "InvalidParameter",
            "message": "the user_id must be a positive integer (Error: " + valid_user_id[-1] +")",
            "status": 400
        })
    
    user_id = int(user_id)
    
    for u in users_db:
        if u['id'] == user_id:
            return jsonify(u)
    
    return jsonify({
        "name": "DataBase",
        "message": "User was not found",
        "status": 404
    })

if __name__ == '__main__':
    res = webbrowser.open('index.html', 2)
    app.run(port='5000')