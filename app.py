from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World - "app" by NLC3U6'
#Feature branch demó - ide lehetne valami fancy új funkciót tenni
app.run(host='0.0.0.0', port=8080)