from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        return f"Hata: templates klasöründe index.html bulunamadı! Detay: {e}"

@socketio.on('message') #sunucu mesaj bekliyor
def handle_message(data):
    emit('message', data, broadcast=True,include_self=False) 

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)

    
