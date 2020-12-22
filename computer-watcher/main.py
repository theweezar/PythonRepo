from flask import Flask, render_template
from flask_socketio import SocketIO, emit
app = Flask(__name__)
socketio = SocketIO(app) 

@app.route('/')
def hello_world():
  return render_template("index.html")

@socketio.on('request_to_connect')
def request_to_connect():
  print("shit")
  emit('connected_to_server', 'connection is established')

if __name__ == "__main__":
  app.run(port = 5005, debug = True)