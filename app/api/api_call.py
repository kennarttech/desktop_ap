import sqlite3
from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()

    if user is not None:
        if user[2] == 1:
            return jsonify({'success': True, 'message': 'Login successful', 'isAdmin': True})
        else:
            return jsonify({'success': True, 'message': 'Login successful', 'isAdmin': False})
    else:
        return jsonify({'success': False, 'message': 'Login failed'})



@app.route('/signup', methods=['POST'])
def signup():
    username = request.json.get('username')
    password = request.json.get('password')
    admin_ = request.json.get('is_admin')

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO users (username, password, is_admin) VALUES (?, ?, 0)", (username, password))
        conn.commit()
        return jsonify({'success': True, 'message': 'Signup successful'})
    except sqlite3.IntegrityError:
        return jsonify({'success': False, 'message': 'Username already exists'})



if __name__ == '__main__':
    conn = sqlite3.connect('users.db')
    conn.execute("CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT, is_admin INTEGER)")
    conn.close()

    app.run(debug=True)
