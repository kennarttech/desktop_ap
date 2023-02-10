from flask import Flask, render_template
from flask_socketio import SocketIO
from flaskwebgui import FlaskUI


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route("/")
def hello():  
    return '<h1>Say hiii to me</h1>'

@app.route("/home")
def home(): 
    return '<h1>Say hiii</h1>'


if __name__ == '__main__':
    # socketio.run(app) for development
    FlaskUI(
        app=app,
        socketio=socketio,
        server="flask_socketio",
        width=800,
        height=600,
    ).run()