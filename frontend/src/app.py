from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    response = requests.get('http://calificaciones-api:8000/calificaciones')
    calificaciones = response.json() if response.status_code == 200 else []
    return render_template('index.html', calificaciones=calificaciones)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)