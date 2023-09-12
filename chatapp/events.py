from .extensions import socketio
from flask_socketio import emit
from flask import request
from chatapp.chatbot.bot import *

users = {}
data, model, data_embeddings = None, None, None

@socketio.on("load_data")
def handle_load_data():
    print("loading data...")
    global data, model, data_embeddings
    data = load_data()
    model = load_model()
    data_embeddings = embeddings_data(data, model)
    # emit("chat", {"username": "system", "message": "BOT READY!"}, broadcast = True)
    emit("dataloaded", True, broadcast=True)

@socketio.on("connect")
def handle_connect():
    print('---------------- Client connected')

@socketio.on("user_join")
def handle_user_join(username):
    print(f"---------------- User {username} joinned!")
    users[username] = request.sid 

@socketio.on("new_message")
def handle_new_message(message):
    print(f'---------------- Receive {message}')

    _bot_reply = getAnswer(message, data, data_embeddings, model)
    print(_bot_reply)
    if _bot_reply['Score'] < 0.8:
        emit("chat", {"message": default_message}, broadcast = True, to = request.sid)    
    else:
        # bot_reply = "\nAnswer:" + _bot_reply['Answer']
        # bot_reply += "\nSimiarity Question:" + _bot_reply['Simiarity Q'] 
        # bot_reply += "\nScore:" + str(_bot_reply['Score'])  
        emit("chat", {"message": _bot_reply["Answer"]}, broadcast = True, to = request.sid)
