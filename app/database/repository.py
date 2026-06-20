from json import dump, load
from pathlib import Path

BASE_DIR = Path(__file__).parent / 'data.json'

async def read_all_notes():
    with open(BASE_DIR, 'r') as f:
        data = load(f)
        return data