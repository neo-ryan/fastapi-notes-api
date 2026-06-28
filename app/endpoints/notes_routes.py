from fastapi import APIRouter, Query
from app.models.notes import Note, NoteResponse
from app.services import notes

router = APIRouter(prefix='/notes')

@router.get('/')
async def note_search(note:str = Query(default=None, min_length=4)) -> list[NoteResponse]:
    if note == None:
        return await notes.get_all()
    else:
        return await notes.note_search(note)

@router.get('/{note_id}')
async def read_note_by_id(note_id:int) -> NoteResponse:
    return await notes.get_by_id(note_id)

@router.post('/')
async def add_note(new_note:Note) -> NoteResponse:
    return await notes.add_note(new_note)

@router.delete('/{note_id}')
async def delete_note(note_id:int) -> list[NoteResponse]:
    return await notes.remove_note(note_id)

@router.put('/{note_id}')
async def update_note() -> NoteResponse:
    pass