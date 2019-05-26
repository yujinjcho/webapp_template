import os

env = os.environ

SECRET_KEY = env['SECRET_KEY']

DB = {
    'dbname': env['DB_NAME'],
    'password': env.get('DB_PASSWORD', None),
    'user': env.get('DB_USER', 'postgres'),
    'port': env.get('DB_PORT', 5432),
    'host': env.get('DB_HOST', 'localhost')
}

GOOGLE_CLIENT_SECRET_CONFIG = env['GOOGLE_CLIENT_SECRET_CONFIG']
GOOGLE_AUTH = {
    'client_id': env['GOOGLE_CLIENT_ID'],
    'client_secret': env['GOOGLE_CLIENT_SECRET'],
    'access_token': env['GOOGLE_ACCESS_TOKEN'],
    'refresh_token': env['GOOGLE_REFRESH_TOKEN'],
    'auth_redirect': env['GOOGLE_AUTH_REDIRECT']
}
