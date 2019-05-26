import calendar
import jwt
from datetime import datetime
from cryptography.fernet import Fernet

from application import app

f = Fernet(app.config['SECRET_KEY'])
date_pattern = '%Y-%m-%d'

def encrypt(s):
    return f.encrypt(s.encode()).decode('utf-8')

def decrypt(s):
    return f.decrypt(s.encode()).decode('utf-8')

def generate_jwt(account_id):
    return jwt.encode({'account_id': account_id}, app.config['SECRET_KEY'], algorithm='HS256').decode('utf-8')

def decode_jwt(encoded):
    try:
        return jwt.decode(encoded, app.config['SECRET_KEY'], algorithms=['HS256'])['account_id'][0]
    except jwt.exceptions.DecodeError:
        return None

def validate_request(request):
    jwt = request.headers.get('X-Auth-Token', 'n/a')
    account_id = decode_jwt(jwt)
    return account_id
