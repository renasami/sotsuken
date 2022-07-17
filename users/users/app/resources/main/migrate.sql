-- drop schema public cascade
-- grant usage on schema public to public;
CREATE SCHEMA IF NOT EXISTS users
\i ./V000_create_table.sql
\i ./V001_it-migrate.sql