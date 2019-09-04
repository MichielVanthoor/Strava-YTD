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
    code = request.request.args.get('code')
    token_response = stravaclient.exchange_code_for_token(client_id=29215, client_secret='9f09fa714a5aa4f9a0950b56ccc2f9d008ce2102', code=code)
    access_token = token_response['access_token']
    refresh_token = token_response['refresh_token']
    expires_at = token_response['expires_at']    

    # Now store that short-lived access token somewhere (a database?)
    client.access_token = access_token
    # You must also store the refresh token to be used later on to obtain another valid access token 
    # in case the current is already expired
    client.refresh_token = refresh_token    

    # An access_token is only valid for 6 hours, store expires_at somewhere and
    # check it before making an API call.
    client.token_expires_at = expires_at
     
    athlete = client.get_athlete()
    print("For {id}, I now have an access token {token}".format(id=athlete.id, token=access_token))

    # name=athlete.id
    name='Michiel'    

    return render_template('authorized.html', name=name)

