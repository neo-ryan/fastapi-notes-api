from fastapi import APIRouter
from app.models.notes import Note, NoteResponse
from app.services import notes

router = APIRouter(prefix='/notes')

@router.get('/')
async def get_notes() -> list[NoteResponse]:
    return await notes.get_all()

@router.get('/{note_id}')
async def read_note_by_id(note_id:int) -> NoteResponse:
    return await notes.get_by_id(note_id)

@router.get('/{note}')
async def note_search(note:str) -> list[NoteResponse]:
    return await notes.note_search(note)

@router.post('/')
async def add_note(new_note:Note) -> NoteResponse:
    return await notes.add_note(new_note)

@router.put('/{note_id}')
async def update_note() -> NoteResponse:
    pass

@router.delete('/{note_id}')
async def delete_note() -> list[NoteResponse]:
    pass