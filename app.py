from flask import Flask, render_template
from flask_scss import Scss
from flask_socketio import join_room, leave_room, send, SocketIO
from datetime import datetime
import random
from string import ascii_uppercase

#App
app = Flask(__name__)
app.config["Secret key"] = "helloworld"
socketio = SocketIO(app)
Scss(app)

@app.route("/", methods=["POST", "GET"])
def home():
    return render_template("landing.html")

if __name__ == "__main__":
    socketio.run(app, debug=True)