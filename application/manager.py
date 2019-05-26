import jwt

from application import app
from application import google_auth
from application import data
from application import helper

def handle_auth_callback(request, session):
    access_token, refresh_token = google_auth.handle_auth_callback(request, session)
    account_id = handle_account(access_token, refresh_token)
    jwt = helper.generate_jwt(account_id)
    base_url = app.config['GOOGLE_AUTH']['auth_redirect']
    redirect_url = '{}?jwt={}'.format(base_url, jwt)
    return redirect_url

def handle_account(access_token, refresh_token):
    user_info = google_auth.get_user_info(access_token, refresh_token)
    email = user_info['email']
    if not email:
        raise Exception('auth user has no email')

    account_ids = data.account_by_email(email)

    if account_ids:
        return account_ids[0]

    data.create_account(email)
    new_account_ids = data.account_by_email(email)
    account_id = new_account_ids[0]
    return account_id
