# CRUD Multi Layered (FastAPI + SQLAlchemy)

This project demonstrates a layered Python web app (controller → service → repository) now migrated to FastAPI and SQLAlchemy with a PostgreSQL backend. It is intended for learning and small demos.

Highlights
- FastAPI-based JSON API (interactive docs at /docs)
- SQLAlchemy ORM for DB access (Postgres)
- Layered architecture: controller → service → repository
- Structured logging configurable via LOG_LEVEL

Security note
IMPORTANT: Passwords are stored in plaintext in this demo. Do NOT use this in production. Replace with bcrypt/argon2 and never return passwords in API responses.

Environment variables (important)
- POSTGRES_USER — DB user
- POSTGRES_PASSWORD — DB password
- POSTGRES_HOST — DB host (for Docker compose this is the service name)
- POSTGRES_DB — DB name
- LOG_LEVEL — optional (DEBUG, INFO, WARNING, ERROR)
- PORT — optional port for the app (defaults to 8000)

API endpoints
- GET  /             — list users (JSON)
- POST /             — create user (JSON body: {name, password})
- GET  /{id}         — get single user
- PUT/PATCH /{id}    — update user (JSON: name and/or password)
- DELETE /{id}       — delete user

How to run (local)
1. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Provide DB environment variables (use `.env` file or export in shell). Example `.env`:

```env
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=localhost
POSTGRES_DB=postgres
LOG_LEVEL=DEBUG
```

4. Start the app:

```bash
python3 app.py
# or run uvicorn directly:
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

How to run with Docker Compose

1. Build and start services:

```bash
docker compose build
docker compose up
```

The API will be available on port 8000 by default (container exposes 8000).

Quick curl examples

Create a user

```bash
curl -X POST http://127.0.0.1:8000/ -H 'Content-Type: application/json' -d '{"name":"alice","password":"pass"}'
```

List users

```bash
curl http://127.0.0.1:8000/
```

Get user

```bash
curl http://127.0.0.1:8000/1
```

Project structure (important files)
- `app.py` — FastAPI app and uvicorn runner
- `controller/user_controller.py` — FastAPI router (API endpoints)
- `service/user_service.py` — business logic and logging
- `repository/user_respository.py` — SQLAlchemy-based DB operations
- `models/user.py` — SQLAlchemy model
- `db/base_model.py` — SQLAlchemy engine, SessionLocal, Base
- `requirements.txt` — Python dependencies

Next recommended improvements
- Hash passwords (bcrypt/argon2) and remove them from API responses
- Add Pydantic models for request/response validation
- Add tests using FastAPI's TestClient
- Add a small entrypoint script to wait for Postgres in Docker before starting the app

License / Disclaimer
This code is educational. Review, test, and harden it before any real deployment.
