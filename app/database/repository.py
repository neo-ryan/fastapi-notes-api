from json import dump, load
from pathlib import Path
from app.models.notes import Note

BASE_DIR = Path(__file__).parent / 'data.json'

async def read_all_notes():
    with open(BASE_DIR, 'r') as f:
        data = load(f)
        return data

async def read_by_id(note_id:int):
    data = await read_all_notes()
    return next((item for item in data if item['id'] == note_id), None)

async def note_search(note:str):
    cleaned = note.strip().lower()
    data =  await read_all_notes()
    found = []
    for item in data:
        if (cleaned in item['title']) or (item['description'] != None and cleaned in item['description']):
            found.append(item)
    return found

async def add_note(new_note:Note):
    new_dict = new_note.model_dump()
    data = await read_all_notes()
    maximum_id = max(data, key=lambda x:x['id'])['id'] if len(data) > 0 else 0
    new_dict['id'] = maximum_id + 1
    data.append(new_dict)
    with open(BASE_DIR, 'w') as f:
        dump(data, f, indent=2)
        f.close()
    return new_dict

async def remove_note(note_id:int):
    data = await read_all_notes()
    
    if any(item['id'] == note_id for item in data):      
        changed_data = [item for item in data if item['id'] != note_id]
        
        with open(BASE_DIR, 'w') as f:
            dump(changed_data, f, indent=2)
            
        return changed_data
    
    else:
        return 'Not Found'
    