from flask import Flask, request

app = Flask(__name__)
last_message = "Hazir"

@app.route('/')
def get_message():
    return last_message

@app.route('/send', methods=['GET', 'POST'])
def post_message():
    global last_message
    if request.method == 'POST':
        last_message = request.data.decode('utf-8')
        return "OK"
    else:
        return '''
            <form method="POST">
                <input name="msg" placeholder="Mesaj yaz" required>
                <button type="submit">Gönder</button>
            </form>
        '''

@app.route('/send-form', methods=['POST'])
def send_form():
    global last_message
    last_message = request.form.get('msg')
    return f"Mesaj gönderildi: {last_message}<br><a href='/send'>Geri dön</a>"

if __name__ == '__main__':
    app.run()
