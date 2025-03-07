from flask import Flask, request
from flask_socketio import SocketIO, emit
from pygame.locals import *
from pygame.draw import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

Clients = {}
game_data = {
    "board": [[None for _ in range(19)] for _ in range(19)],
    "turn": False,
    "isPlaying": True
}

@socketio.on('connect')
def on_connect():
    sid = request.sid
    Clients[sid] = Clients.get(sid, 'user')
    print(f'Client {sid} connected')

@socketio.on('disconnect')
def on_disconnect():
    sid = request.sid
    if sid in Clients:
        del Clients[sid]
    print(f'Client {sid} disconnected')

@socketio.on('make_move')
def on_make_move(data):
    x_idx, y_idx, color = data['x_idx'], data['y_idx'], data['color']
    if game_data["board"][x_idx][y_idx] is None and game_data["isPlaying"]:
        game_data["board"][x_idx][y_idx] = color
        game_data["turn"] = not game_data["turn"]
        
        # Check for win
        if check_win(x_idx, y_idx, color):
            emit('game_over', {'winner': color})
        else:
            emit('update_board', game_data["board"])

def check_win(x_idx, y_idx, color):
    directions = [
        (1, 0),  # Horizontal
        (0, 1),  # Vertical
        (1, 1),  # Diagonal /
        (1, -1)  # Diagonal \
    ]
    for dx, dy in directions:
        count = 1  # Include the current stone
        for i in range(1, 5):  # Check in one direction
            nx, ny = x_idx + dx * i, y_idx + dy * i
            if 0 <= nx < 19 and 0 <= ny < 19 and game_data["board"][nx][ny] == color:
                count += 1
            else:
                break
        for i in range(1, 5):  # Check in the opposite direction
            nx, ny = x_idx - dx * i, y_idx - dy * i
            if 0 <= nx < 19 and 0 <= ny < 19 and game_data["board"][nx][ny] == color:
                count += 1
            else:
                break
        if count >= 5:
            return True
    return False

if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', debug=True)