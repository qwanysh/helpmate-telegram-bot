from functools import wraps
from logging import getLogger

from .config import MY_TELEGRAM_ID
from .exceptions import MessageError


logger = getLogger()


def handle_errors(func):
    @wraps(func)
    async def wrapper(update, context):
        try:
            await func(update, context)
        except MessageError as error:
            await update.message.reply_text(error.message)
        except Exception as error:
            logger.exception(error)
            await update.message.reply_text('Something went wrong')

    return wrapper


def guard(func):
    @wraps(func)
    async def wrapper(update, context):
        telegram_id = update.message.from_user.id

        if telegram_id == MY_TELEGRAM_ID:
            await func(update, context)

    return wrapper
