from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/Users/sakaitaiki/desktop/on_hand_test')
def home():
    return "I'm alive"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()