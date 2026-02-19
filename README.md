# efield-practice-app

Pilot web app for General Physics 2 electric field practice with randomized 4-charge problems, auto-grading, and attempt history.

## Stack
- Python 3.11+
- Flask
- SQLAlchemy 2.x
- Alembic
- gunicorn
- pytest

## Local setup
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Environment variables
Required:
- `SECRET_KEY` - Flask session secret.
- `ADMIN_TOKEN` - token used for `/admin/export.csv?token=...`.

Optional:
- `DATABASE_URL` - database connection string.
  - If unset, app falls back to local SQLite at `sqlite:///app.db`.

## Database migrations
```bash
alembic upgrade head
```

## Run locally
```bash
flask --app wsgi run
```

## Run tests
```bash
pytest
```

## Production (Render)
### Render Web Service
- Build command:
  ```bash
  pip install -r requirements.txt && alembic upgrade head
  ```
- Start command:
  ```bash
  gunicorn wsgi:app
  ```

### Render Postgres
- Provision Render Postgres and set web service environment variable:
  - `DATABASE_URL=<render postgres internal url>`
- Also set:
  - `SECRET_KEY`
  - `ADMIN_TOKEN`

## App routes
- `GET /` landing page to enter `user_code`.
- `POST /set_user` sets `user_code` in session.
- `GET /change_user` clears session and resets current user.
- `GET /problem` generates a pure-random new problem each visit.
- `POST /submit` grades Ex/Ey with default 3% component tolerance and stores attempt.
- `GET /history` shows current user attempt history.
- `GET /admin/export.csv?token=...` exports all attempts as CSV.

## Physics model
- Four point charges, one in each quadrant.
- Coordinates use integer grid points with signs by quadrant:
  - x and y magnitudes each sampled from `{1, 2}`.
- Charge values sampled from `{±1, ±2, ±3}` nC.
- Target point is the Q1 charge location.
- Field uses other three charges only and Coulomb vector form:
  - `E = k q r_vec / r^3`
- Constants:
  - `k = 8.9875517923e9 N m^2 / C^2`
  - `1 nC = 1e-9 C`
  - `GRID_SPACING_M = 0.10`
- Returns `Ex`, `Ey` in `N/C`.
