import dotenv
import os
import psycopg2
import sqlalchemy as alchemy
from models.decalreDB import Base
from controller.TenantController import Tenant_Controller

env = dotenv.load_dotenv(".env")

pg_host = os.getenv("pg_host")
pg_role = os.getenv("pg_role")
pg_pass = os.getenv("pg_pass")
pg_base = os.getenv("pg_base")
alchemy_uri = f"postgresql+psycopg2://{pg_role}:{pg_pass}@{pg_host}/{pg_base}?sslmode=require&channel_binding=require"

pg_uri = f"postgresql://{pg_role}:{pg_pass}@{pg_host}/{pg_base}?sslmode=require&channel_binding=require"

def test_engine(uri):
    engine = alchemy.create_engine(uri)
    with engine.connect() as conn :
        res = conn.execute(alchemy.text("SELECT version()"))
        conn.commit()
        if res :
            return True
        else :
            return False

def test_conn(uri):

    conn = psycopg2.connect(uri)
    with conn.cursor() as cur:
        cur.execute("select version()")
        print(cur.fetchone())
    conn.close()

tenant = Tenant_Controller.read(2)
