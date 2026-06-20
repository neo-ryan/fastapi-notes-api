from fastapi import FastAPI
from app.endpoints import notes_routes

app = FastAPI(
    title='Notes API',
    description='CRUD API for note-taking',
    version='1.0',
)

app.include_router(notes_routes.router)