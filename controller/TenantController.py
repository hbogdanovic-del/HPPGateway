import datetime
from sqlalchemy.orm import Session
from sqlalchemy import engine
from models.tenant import Tenant
import conf as cf

class Tenant_Controller:

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
