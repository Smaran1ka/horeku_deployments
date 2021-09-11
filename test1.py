from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'helo world'

@app.route('/hello')
def hello():
    return 'reached the hello world page'

app.run()