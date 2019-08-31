from app import app

import os

from flask import render_template, request
from flask_sslify import SSLify
from werkzeug.contrib.fixers import ProxyFix

# Configure HTTPS redirect
app.wsgi_app = ProxyFix(app.wsgi_app)
SSLify(app)

# Overview of all the routes
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
