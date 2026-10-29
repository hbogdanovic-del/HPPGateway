from fastapi import FastAPI
from controller.TenantController import Tenant_Controller

app = FastAPI()

@app.get("/")
def read_root():
    return {"mess": "Hello World !"}

@app.get("/tenant/{id}")
def get_tenant_from_id(id: int):
    tenant = Tenant_Controller.read(id)
    return {"tenant": f"{tenant}"}
