import json
from flask import g
import psycopg2
from psycopg2.extras import execute_values

from application import app

def store_auth_token(account_id, token):
    query = """
      UPDATE account
        SET google_auth_token = %s
      WHERE account_id = %s
    """
    return _insert(query, (token, account_id))

def account_by_email(email):
    query = """
      SELECT account_id
      FROM account
      WHERE email = %s
    """
    return _select(query, (email,))

def create_account(email):
    print('creating account')
    query = """
      INSERT INTO account (email)
        VALUES (%s)
    """
    return _insert(query, (email,))

def _insert(query, params):
    db = _connection()
    try:
        with db.cursor() as cur:
            cur.execute(query, params)
            updated_rows = cur.rowcount
        cur.close()
        db.commit()
    finally:
        db.close()

    return updated_rows

def _select(query, params = None):
    try:
        db = _connection()
        with db.cursor() as cur:
            if params:
                cur.execute(query, params)
            else:
                cur.execute(query)

            results = cur.fetchall()
        cur.close()
    finally:
        db.close()

    return results

def _connection():
    return psycopg2.connect(**app.config['DB'])
