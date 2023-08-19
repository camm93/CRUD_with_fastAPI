# Simple CRUD with FastAPI, Postgresql, and Docker.

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

## FastAPI Docker Application with PostgreSQL
This repository contains a simple FastAPI application running in a Docker container, connected to a PostgreSQL database running in another Docker container.

### Prerequisites
Docker installed on your machine
Basic understanding of Docker and PostgreSQL


### Getting Started
1. Clone this repository:

bash
git clone https://github.com/camm93/CRUD_with_fastAPI.git
cd CRUD_with_fastAPI

2. Create a .env file in the root directory with your PostgreSQL database configuration:

DATABASE_URL=postgresql://postgres:yourpassword@postgres:5432/db_name
Replace yourpassword with your desired password.

3. Build and run the Docker containers using docker-compose:

docker-compose up -d --build

4. Access the FastAPI application at http://localhost:8000.

5. To shut down the containers:

docker-compose down

### Configuration
**FastAPI Application**: The FastAPI application is defined in the app directory. You can modify the routes and logic in the main.py file.

**PostgreSQL Configuration**: PostgreSQL configuration settings can be found in the docker-compose.yml file. The POSTGRES_DB, POSTGRES_USER, and POSTGRES_PASSWORD environment variables can be modified to suit your needs.

**Database Connection**: The connection to the PostgreSQL database is established using the DATABASE_URL defined in the .env file. Ensure that the URL matches your PostgreSQL configuration.

**Database Initialization**: The init.sql script in the postgres/init directory is executed when the PostgreSQL container starts. You can modify this script to create tables and populate initial data.

**Network Configuration**: By default, the containers are connected to the same default bridge network. Modify the docker-compose.yml file's networks section if you want to customize the network configuration.

#### Troubleshooting
- If you encounter connection issues between the FastAPI application and the PostgreSQL container, ensure that the IP address and port in the pg_hba.conf file (inside the PostgreSQL container) match the values in your DATABASE_URL.

- Check the logs of both containers using docker-compose logs <container_name> to diagnose any errors.

## Extra

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
