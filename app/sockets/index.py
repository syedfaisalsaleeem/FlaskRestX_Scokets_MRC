from app import sk
from flask_socketio import emit,join_room,leave_room
import json
rooms_list = []

@sk.on('connect')
def test_message():
    print("connect")
    print('[INFO] Web client connected: ')


@sk.on('disconnect')
def test_disconnect():
    print("----client disconnected ---")

@sk.on('createrooms')
def create_room(data):
    try:
        data = json.loads(data)
        room = str(data['room'])
        if room not in rooms_list:
            print("----room created ---")
            join_room(room)
            rooms_list.append(room)
            emit('createroom',room+' room has been created', broadcast=False)
    except Exception as e:
        print("----error---",e)

@sk.on('join')
def on_join(data):
    try:
        data = json.loads(data)
        username = data['username']
        room = data['room']
        if room in rooms_list:
            join_room(room)
            emit("global1",username + ' has entered the room.', broadcast=True)
        else:
            emit("global1","this room is not created ", broadcast=True)
    except Exception as e:
        print("----error---",e)

@sk.on('leave')
def on_leave(data):
    try:
        data = json.loads(data)
        username = data['username']
        room = data['room']
        leave_room(room)
        emit("global1",username + ' has left the room.', to=room)
    except Exception as e:
        print("----error---",e)