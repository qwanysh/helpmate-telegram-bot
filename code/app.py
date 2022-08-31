from telegram.ext import ApplicationBuilder, CommandHandler

from .config import TOKEN
from .handlers import handle_spend, handle_today

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler('spend', handle_spend))
app.add_handler(CommandHandler('today', handle_today))
