# Simple CRUD with FastAPI and Postgresql.

Designed to:
- Run both the app and database locally.
- Containerized app + local database ```use docker-compose-local-db.yml```.
- Containerized app and database  ```use docker-compose-containers.yml```.

*Just remove "-local-db" or "-containers" from yml filenames*

**Opt1**. To run the server in local machine:
``uvicorn main:app --reload``

**Opt2 and 3**.
- Create the images by ``docker-compose up --build``
- ``docker-compose down`` will stop and remove the containers created by previous docker-compose up, but will keep the images.

**execute container: Open container terminal**
docker exec -it practice-postgres bash

**start postgres console**
psql -U postgres

\h help with SQL commands
\? help with Psql commands

**Useful commands inside postgres container terminal**
- create database dbname;
- create user myuser with encrypted password 'mypassword';
- grant all privileges on database mydbname to myuser;
- \l list databases
- \du list users
- \c mydbname;  --> This connect to db
- \dt --> list tables in db
- psql -h localhost -p 5432 postgres  --> To make this db available outside the container


- \q to quit postgres
- *exit* to exit the terminal


Get local IP address
    ipconfig (Dirección IPv4)

*Inspired by*
[Create A REST API with FastAPI, SQLAlchemy and PostgreSQL](https://www.youtube.com/watch?v=2g1ZjA6zHRo&t=1443s&ab_channel=SsaliJonathan)
