CREATE TABLE account (
  account_id SERIAL PRIMARY KEY,
  email TEXT
);

CREATE UNIQUE INDEX ON account (email);
