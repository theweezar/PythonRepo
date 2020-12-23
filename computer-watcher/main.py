from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import numpy as np
import cv2
import time
import base64
from PIL import Image
from io import BytesIO
app = Flask(__name__)
socketio = SocketIO(app) 
fps = 1/60
app.config['streaming'] = False

@app.route('/')
def hello_world():
  # app.logger.info('Conntection is established')
  return render_template("index.html")

@socketio.on('connect')
def connect():
  app.logger.info('Conntection is established')

@socketio.on('start_webcam')
def start_webcam():
  cap = cv2.VideoCapture(0)
  app.config['streaming'] = True
  # Kiểm tra camera
  if not cap.isOpened:
    app.config['streaming'] = False
    emit('error_camera_not_open')
  else:
    ret, frame = cap.read()
    if not ret:
      app.config['streaming'] = False
      emit('cant_get_frame')
  while app.config['streaming']:
    ret, frame = cap.read()
    if not ret:
      emit('cant_get_frame')
      break
    # ret, buffer = cv2.imencode('.jpg', frame)
    # array_buffer = base64.b64encode(buffer.tobytes())
    frame = frame[:,::-1]
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    pil_img = Image.fromarray(frame)
    buff = BytesIO()
    pil_img.save(buff, format="JPEG")
    new_image_string = base64.b64encode(buff.getvalue()).decode("utf-8")
    emit('recording', new_image_string)
    time.sleep(fps)

@socketio.on('stop_webcam')
def stop_webcam():
  app.config['streaming'] = False

if __name__ == "__main__":
  # Phải set host = '0.0.0.0' thì mới có thể public trong network được
  socketio.run(app, port=5000, debug=True, host='192.168.1.2')