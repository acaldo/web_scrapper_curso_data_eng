CREATE TABLE newspaper (
  id serial PRIMARY KEY,
  title text NOT NULL,
  author text NOT NULL,
  content text NOT NULL
);

COPY newspaper FROM '/newspaper.csv' WITH (FORMAT csv);
