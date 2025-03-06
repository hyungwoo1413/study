from flask import Flask,request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

Clients = {}

@socketio.on('connect')
def on_connect():
    sid = request.sid
    Clients[sid] = Clients.get(sid,'user')

@socketio.on('disconnect')
def on_disconnect():
    pass

@socketio.on('double')
def on_doulbe(data):
    temp = data * 2
    emit('take', temp)

if __name__ == "__main__":
    socketio.run(app,host='127.0.0.1',debug=True)