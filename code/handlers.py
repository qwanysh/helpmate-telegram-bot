from .decorators import guard, handle_errors
from .helpers import render
from .utils import create_spending, parse_spending


@guard
@handle_errors
async def handle_spend(update, context):
    await create_spending(**parse_spending(update.message.text))
    await update.message.reply_text(render('handle_spend'))
