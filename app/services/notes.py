from app.database import repository
from fastapi import HTTPException
from app.models.notes import Note

async def get_all():
    return await repository.read_all_notes()

async def get_by_id(note_id:int):
    receive = await repository.read_by_id(note_id)
    if receive != None:
        return receive
    else:
        raise HTTPException(status_code=404)

async def note_search(note:str):
    receive = await repository.note_search(note)
    if receive != []:
        return receive
    else:
        raise HTTPException(status_code=404)

async def add_note(new_note:Note):
    return await repository.add_note(new_note)