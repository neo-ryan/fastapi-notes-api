from pydantic import BaseModel, Field
from typing import Annotated

class Note(BaseModel):
    title:Annotated[str, Field(max_length=20), 'Note title']
    description:Annotated[str | None, Field(max_length=150), 'Details'] = None
    tags:list[str] | None = []

class NoteResponse(Note):
    id:Annotated[int, 'Note ID']