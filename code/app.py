from telegram.ext import ApplicationBuilder, CommandHandler

from .config import TOKEN
from .handlers import handle_spend

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler('spend', handle_spend))
