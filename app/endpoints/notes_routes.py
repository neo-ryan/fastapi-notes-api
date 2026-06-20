from fastapi import APIRouter
from app.models.notes import Note, NoteResponse
from app.services import notes

router = APIRouter(prefix='/notes')

@router.get('/')
async def get_notes() -> list[NoteResponse]:
    return await notes.get_all()

@router.get('/{note_id}')
async def read_note() -> NoteResponse:
    pass

@router.post('/')
async def add_note() -> NoteResponse:
    pass

@router.put('/{note_id}')
async def update_note() -> NoteResponse:
    pass

@router.delete('/{note_id}')
async def delete_note() -> list[NoteResponse]:
    pass