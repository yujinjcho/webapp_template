import jwt

from application import app
from application import google_auth
from application import data
from application import helper

def handle_auth_callback(request, session):
    access_token, refresh_token = google_auth.handle_auth_callback(request, session)
    account_id = handle_account(access_token, refresh_token)
    return helper.generate_jwt(account_id)

def handle_account(access_token, refresh_token):
    user_info = google_auth.get_user_info(access_token, refresh_token)
    email = user_info['email']
    if not email:
        raise Exception('auth user has no email')

    account_ids = data.account_by_email(email)
    encrypted_token = helper.encrypt(access_token)
    encrypted_refresh_token = helper.encrypt(refresh_token) if refresh_token else None

    if account_ids:
        data.update_account(account_ids[0], encrypted_token, encrypted_refresh_token)
        return account_ids[0]

    data.create_account(email, encrypted_token, encrypted_refresh_token)
    new_account_ids = data.account_by_email(email)
    account_id = new_account_ids[0]
    return account_id
