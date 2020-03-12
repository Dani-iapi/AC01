
# A very simple Flask Hello World app for you to get started with...

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'AC 01!'

@app.route('/home')
def inicio():
    return render_template ('inicio.html')