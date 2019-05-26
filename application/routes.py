import os

from flask import jsonify, request, redirect, session, abort, render_template

from application import app
from application import helper
from application import google_auth
from application import manager

@app.route('/', methods=['GET'])
def root():
#     return render_template('index.html')
    return 'Ok'


@app.route('/api/auth/login', methods=['GET'])
def auth_login():
    return jsonify({'result': google_auth.auth_url(session)})

@app.route('/api/auth/callback', methods=['GET'])
def auth_callback():
    jwt = manager.handle_auth_callback(request, session)
    base_url = app.config['GOOGLE_AUTH']['auth_redirect']
    url = '{}?jwt={}'.format(base_url, jwt)
    return redirect(url)

@app.route('/api/auth/user_info', methods=['GET'])
def auth_user_info():
    access_token = app.config['GOOGLE_AUTH']['access_token']
    refresh_token = app.config['GOOGLE_AUTH']['refresh_token']
    res = google_auth.get_user_info(access_token, refresh_token)
    return jsonify(res)

@app.route('/api/validate/account', methods=['GET'])
def validate_account():
    account_id = helper.validate_request(request)
    response = jsonify({'result': account_id}) if account_id else abort(400)
    return response

# @app.route('/<path:path>')
# def catch_all(path):
#     return render_template('index.html')
