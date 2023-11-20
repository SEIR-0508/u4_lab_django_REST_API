-- settings.sql
CREATE DATABASE rest_api;
CREATE USER rest_api_user WITH PASSWORD 'rest_api';
GRANT ALL PRIVILEGES ON DATABASE rest_api TO rest_api_user;