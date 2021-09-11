from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('home.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/Gallery')
def gallery():
    return render_template('gallery.html')

app.run(debug=True)