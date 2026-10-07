import os

user = os.environ["POSTGRES_USER"]
password = os.environ["POSTGRES_PASSWORD"]
database = os.environ["POSTGRES_DB"]

DATABASE_URL = (
    f"postgresql+asyncpg://{user}:{password}@db:5432/{database}"
)

if not DATABASE_URL:
    raise RuntimeError("Отсутствует ссылка на базу данных")