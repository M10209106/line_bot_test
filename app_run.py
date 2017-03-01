import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return os.environ.get('SECRET_KEY', 'this_should_be_configured')