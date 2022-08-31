from .decorators import guard, handle_errors
from .helpers import reply_rendered_text
from .utils import (
    create_spending, get_today_spendings_by_categories, parse_spending,
)


@guard
@handle_errors
async def handle_spend(update, context):
    await create_spending(**parse_spending(update.message.text))
    await update.message.reply_text('Spending saved')


@guard
@handle_errors
async def handle_today(update, context):
    spendings = await get_today_spendings_by_categories()
    total_amount = sum(spending['total'] for spending in spendings)
    await reply_rendered_text(
        update, 'total_by_categories',
        spendings=spendings, total_amount=total_amount,
    )
