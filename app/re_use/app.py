from flask import Flask, jsonify, request

app = Flask(__name__)

students = [
    {
        'id': 1,
        'name': 'Alice',
        'age': 21,
        'major': 'Computer Science'
    },
    {
        'id': 2,
        'name': 'Bob',
        'age': 22,
        'major': 'Engineering'
    },
    {
        'id': 3,
        'name': 'Charlie',
        'age': 23,
        'major': 'Mathematics'
    }
]

@app.route('/')
def home():
    return 'welcome home'


@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)



users = {
    "user1": {"password": "password1", "is_admin": True, "user_id": 1},
    "user2": {"password": "password2", "is_admin": False, "user_id": 2}
}

data = {}



@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    if username in users and users[username]['password'] == password:
        return jsonify(users[username])
    return '', 401



@app.route('/data', methods=['GET'])
def get_data():
    user_id = request.args.get('user_id')
    print(dir(user_id))
    if user_id is None:
        return jsonify(data)
    else:
        user_data = [item for item in data.values() if item['user_id'] == int(user_id)]
        return jsonify(user_data)




@app.route('/data', methods=['POST'])
def save_data():
    data_item = request.json
    data_item['user_id'] = request.json.get('user_id')
    data[len(data) + 1] = data_item
    return '', 201



@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    for student in students:
        if student['id'] == student_id:
            return jsonify(student)
    return jsonify({'Error': 'Student not found in the system'})



@app.route('/students', methods=['POST'])
def add_student():
    student = {
        'id': request.json['id'],
        'name': request.json['name'],
        'age': request.json['age'],
        'major': request.json['major']
    }
    students.append(student)
    return jsonify({'Message': 'Student added successfully'})



if __name__ == '__main__':
    app.run(debug=True)
