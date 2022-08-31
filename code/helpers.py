from tortoise import run_async, Tortoise

from .config import DATABASE_URL, jinja2_env


def connect_database():
    run_async(Tortoise.init(
        db_url=DATABASE_URL,
        modules={
            'models': ['code.models'],
        },
    ))


async def reply_rendered_text(update, template_name, **kwargs):
    template = jinja2_env.get_template(f'{template_name}.html')
    await update.message.reply_text(
        template.render(**kwargs), parse_mode='html',
    )
