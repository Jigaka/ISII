import json
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

entorno = '.env.prod.json' if Path(f'{BASE_DIR}/.env.prod.json').exists() else '.env.dev.json'

def get_credentials():
    env_file_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(os.path.join(env_file_dir, entorno), 'r') as f:
        creds = json.loads(f.read())
    return creds


credentials = get_credentials()