from flask import Flask, request

app = Flask(__name__)
last_message = "Hazir"

@app.route('/')
def home():
    return f"""
    <h2>LCD Ekran Mesajı:</h2>
    <p>{last_message}</p>
    <form action="/send" method="post">
        <input type="text" name="message" placeholder="Mesaj yaz" required>
        <button type="submit">Gönder</button>
    </form>
    """

@app.route('/send', methods=['POST'])
def send():
    global last_message
    if request.form.get('message'):
        last_message = request.form.get('message')
    else:
        last_message = request.data.decode('utf-8')
    return "OK"

@app.route('/text', methods=['GET'])
def text():
    return last_message

if __name__ == '__main__':
    app.run()
