import os

from flask import jsonify, request, redirect, session, abort, render_template

from application import app, google_auth, helper, manager

@app.route('/', methods=['GET'])
def root():
    return 'Ok'

@app.route('/api/auth/login', methods=['GET'])
def auth_login():
    return jsonify({'result': google_auth.auth_url(session)})

@app.route('/api/auth/callback', methods=['GET'])
def auth_callback():
    redirect_url = manager.handle_auth_callback(request, session)
    return redirect(redirect_url)

@app.route('/api/validate/account', methods=['GET'])
def validate_account():
    account_id = helper.validate_request(request)
    response = jsonify({'result': account_id}) if account_id else abort(400)
    return response
