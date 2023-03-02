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
    app.run(debug=True, host='0.0.0.0', port=4000)
