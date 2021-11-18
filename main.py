from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home.html')


@app.route('/dodaj')
def add_page():
    return render_template('dodaj.html')