
psql -U postgres -c 'CREATE DATABASE my_db'

psql -U postgres -d my_db -f init_db.sql
