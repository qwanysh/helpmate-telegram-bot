import os
import pathlib

from dotenv import load_dotenv
import jinja2

load_dotenv()

BASE_DIR = pathlib.Path()

TOKEN = os.getenv('TOKEN')

DATABASE_URL = os.getenv('DATABASE_URL')

MY_TELEGRAM_ID = int(os.getenv('MY_TELEGRAM_ID'))

HEROKU_APP_NAME = os.getenv('HEROKU_APP_NAME')

HEROKU_PORT = os.getenv('PORT')

TORTOISE_ORM = {
    'connections': {'default': DATABASE_URL},
    'apps': {
        'models': {
            'models': ['code.models', 'aerich.models'],
            'default_connection': 'default',
        },
    },
}

jinja2_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(BASE_DIR / 'templates'),
    trim_blocks=True, lstrip_blocks=True,
)
