import datetime
from sqlalchemy.orm import Session
from sqlalchemy import engine, select
from models.tenant import Tenant
import conf as cf
from pydantic import BaseModel

class Tenant_Controller(BaseModel):

    def create(nom:str, mail:str) -> Tenant :
        timestamp = datetime.datetime.now()
        if not nom.isalpha() :
            raise Exception("Le nom doit etre au format alphanumerique")
        elif not mail.isascii() :
            raise Exception("Le mail doit etre au format ASCII")
        tenant = Tenant(nom=nom, mail=mail, created_at=timestamp)
        cf.session.add(tenant)
        cf.session.commit()
        return tenant

    def read(id:int) -> Tenant:
        stmt=select(Tenant).where(Tenant.id == id)
        res = cf.session.scalars(stmt)
        res = res.fetchall()
        if len(res > 1):
            raise Exception("Plus d'une ligne trouvé")
        return res

