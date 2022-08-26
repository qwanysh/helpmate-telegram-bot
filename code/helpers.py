from tortoise import run_async, Tortoise

from .config import DATABASE_URL, jinja2_env


def connect_database():
    run_async(Tortoise.init(
        db_url=DATABASE_URL,
        modules={
            'models': ['code.models'],
        },
    ))


def render(template_name, **kwargs):
    template = jinja2_env.get_template(f'{template_name}.html')
    return template.render(**kwargs)
