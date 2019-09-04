from app import app

import os

from flask import render_template, request, url_for, redirect
from flask_sslify import SSLify
from stravalib.client import Client
from werkzeug.contrib.fixers import ProxyFix

# Configure HTTPS redirect
app.wsgi_app = ProxyFix(app.wsgi_app)
SSLify(app)

# Initialize Strava Client
stravaclient = Client()
domain = 'app-45w2jmzzla-ew.a.run.app'

# Overview of all the routes
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return redirect(stravaclient.authorization_url(client_id=29215, redirect_uri='https://app-45w2jmzzla-ew.a.run.app/authorized'))

@app.route('/authorized')
def authorized():
    return render_template('index.html')

