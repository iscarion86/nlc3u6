from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World - "app" by NLC3U6'

app.run(host='0.0.0.0', port=8080)