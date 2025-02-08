# CRUD Multi Layered

This project has created to study multi layers in python using *docker* to up server web flask and database *postgres*.

this application use .env file to security.

## Endpoints


`POST /`

    register new user , using fields "name"  and "password"

# CRUD Multi Layered

Minimal Flask app demonstrating a layered architecture (controller → service → repository) using Peewee and a relational database.

This repository is intended for learning and small demos. It includes a responsive Bootstrap UI, inline modal updates, and structured logging to help debug features.

## Features
- Create users (simple username + password model)
- List users in a responsive table
- Update users inline using a Bootstrap modal (same-page UX)
- Delete users from the list
- Structured logging (console) with configurable log level

IMPORTANT: This project stores passwords in plaintext for demonstration only. Do NOT use this approach in production — always hash passwords (bcrypt/argon2) and never display them.

## Environment variables
- SECRET_KEY: required by Flask-WTF for CSRF protection
- FLASK_DEBUG: control Flask debug mode (1/0)
- FLASK_APP: Flask app path (not required to run via `python app.py`)
- POSTGRES_DB: database name (if using Docker-compose postgres)
- POSTGRES_USER: DB user
- POSTGRES_PASSWORD: DB password
- POSTGRES_HOST: DB host
- LOG_LEVEL: optional, logging level (DEBUG, INFO, WARNING, ERROR). Default: DEBUG

## Endpoints / UI
- GET / — main page: registration form (left) and users table (right). Update opens a modal.
- POST / — same endpoint handles create, delete and update actions (POST form fields determine action)

Notes on forms
- Registration form uses `LoginForm` (username, password)
- Update form uses `UpdateForm` and is submitted from a modal on the same page. The controller recognizes the hidden `update` field to perform the update.

## How to run
1. (Optional) Create a `.env` file with the environment variables listed above.
2. To run locally without Docker:

```bash
python3 app.py
```

3. To run with Docker Compose (if you have a docker-compose setup with Postgres configured):

```bash
docker compose up
```

You can control logging verbosity with:

```bash
export LOG_LEVEL=INFO 
python3 app.py
```

## Project structure (important files)
- `app.py` — Flask app and logging configuration
- `controller/user_controller.py` — routes and request handling
- `service/user_service.py` — business logic and exception logging
- `repository/user_respository.py` — DB operations (Peewee)
- `models/user.py` — Peewee model
- `templates/index.html` — responsive UI and update modal

## License / Disclaimer
This code is educational. Review and harden it before any real deployment.
