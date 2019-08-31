from app import app

import firebase_admin
import os

from firebase_admin import credentials
from firebase_admin import firestore
from flask import render_template, request
from flask_sslify import SSLify
from werkzeug.contrib.fixers import ProxyFix

# Configure HTTPS redirect
app.wsgi_app = ProxyFix(app.wsgi_app)
SSLify(app)

# Use the application default credentials and connect db
cred = credentials.ApplicationDefault()
if 'PROJECT_ID' in os.environ:
    print('Staging area: ' + os.environ['PROJECT_ID'])
    firebase_admin.initialize_app(cred, {
        'projectId': os.environ['PROJECT_ID']
    })
    db = firestore.client()


# Overview of all the routes
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/over_ons')
def about_us():
    return render_template('about_us.html')


@app.route('/projects')
def projects():
    projects = db.collection(u'projects').order_by(u'date').steam()

    return render_template('projects.html', projects=projects)
