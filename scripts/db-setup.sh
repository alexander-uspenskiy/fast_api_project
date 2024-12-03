#!/bin/sh

export PGUSER="postgres"

psql -c "CREATE DATABASE inventory;"


psql -d inventory -c "CREATE TABLE test (id SERIAL PRIMARY KEY, name TEXT);"

psql -d inventory -c "INSERT INTO test (name) VALUES ('First test');"


psql -c "CREATE EXTENSION IF NOT EXIST \"uuid-ossp"\";"