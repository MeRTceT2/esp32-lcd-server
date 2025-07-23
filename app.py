from flask import Flask, request

app = Flask(__name__)
last_message = "Hazir"

@app.route('/')
def get_message():
    return f"""
    <h2>LCD Ekran Mesajı:</h2>
    <p>{last_message}</p>
    <form action="/send" method="post">
        <input type="text" name="message" placeholder="Mesaj yaz" required>
        <button type="submit">Gönder</button>
    </form>
    """

@app.route('/send', methods=['POST'])
def post_message():
    global last_message
    # Hem formdan hem ESP'den gelen veriyi destekle
    if request.form.get('message'):
        last_message = request.form.get('message')
    else:
        last_message = request.data.decode('utf-8')
    return "OK"
