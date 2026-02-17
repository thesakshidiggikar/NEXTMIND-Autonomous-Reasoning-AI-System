from fastapi import FastAPI
from api.routes import router

app = FastAPI(title="NEXTMIND API")

app.include_router(router)
