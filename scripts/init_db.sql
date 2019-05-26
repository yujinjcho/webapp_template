
CREATE TABLE account (
  account_id SERIAL PRIMARY KEY,
  account_name TEXT,
  email TEXT,
  google_auth_token TEXT,
  google_refresh_token TEXT
);

CREATE UNIQUE INDEX ON account (email);
CREATE UNIQUE INDEX ON account (account_id, google_auth_token);
