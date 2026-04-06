from flask import Flask, render_template
import os
import codecs

app = Flask(__name__)

# Routes
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)