# Web app template

Generic template for a react web app backed by a flask backend and postgres database. User management handled by google oauth.

### Database
Requires postgres and psql command.

Inside `scripts` dir.
```
./init_db.sh
```

### Flask backend

Install python dependencies.
```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

Generate certificates. Inside `scripts` dir. Allows serving requests over https (required for google auth).

```
./generate_keys.sh
```

Running flask app.
```
SECRET_KEY={KEY} \ # for encrypt/decrypt i.e. Fernet.generate_key()
DB_NAME='my_db' \
GOOGLE_CLIENT_SECRET_CONFIG='{}' \ # json format
GOOGLE_CLIENT_ID={GOOGLE_CLIENT_ID} \
GOOGLE_CLIENT_SECRET={GOOGLE_CLIENT_SECRET} \
GOOGLE_AUTH_REDIRECT='http://localhost:3000/auth' \
  python run.py

```

### React frontend

Inside `front` dir.

```
npm install
npm start
```


