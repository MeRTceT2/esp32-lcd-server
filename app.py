from flask import Flask, request

app = Flask(__name__)
last_message = "Hazir"

@app.route('/')
def get_message():
    return last_message

@app.route('/send', methods=['POST'])
def post_message():
    global last_message
    last_message = request.data.decode('utf-8')
    return "OK"
