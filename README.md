# FastAPI + PostgreSQL production ready setup

**database setup:**

take a look at `app/core/config.py` and add necessary db credentials

Install all packages

`pip install -r requirements.txt`

**Migrations setup:**

### Create folder named `versions` in `migrations` folder

initial migration commands (if you make any changes in models or `migrations/versions` doesn't have any file):

`alembic revision --autogenerate -m "migration message"`

`alembic upgrade head`

Run the following command if `migrations/versions` has some files in it:

`alembic upgrade head`

Run the project:

`uvicorn main:app --reload`
