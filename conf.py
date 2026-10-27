import dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

env = dotenv.load_dotenv(".env")

pg_host = os.getenv("pg_host")
pg_role = os.getenv("pg_role")
pg_pass = os.getenv("pg_pass")
pg_base = os.getenv("pg_base")
alchemy_uri = f"postgresql+psycopg2://{pg_role}:{pg_pass}@{pg_host}/{pg_base}?sslmode=require&channel_binding=require"

engine = create_engine(alchemy_uri)
session = sessionmaker(bind=engine)
session = session()
