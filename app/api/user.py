from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api')
def my_api():
    data = {'name': 'John', 'age': 30, 'is_student': True, 'hobbies': ['reading', 'playing guitar', 'traveling']}
    return jsonify(data)

    

if __name__ == '__main__':
    app.run()
