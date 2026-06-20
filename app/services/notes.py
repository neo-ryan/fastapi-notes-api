from app.database import repository

async def get_all():
    return await repository.read_all_notes()