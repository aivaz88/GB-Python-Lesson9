from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def log(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = open('db.csv', 'a')
    file.write(f'{update.effective_user.first_name}, {update.effective_user.id}, {update.message.text}\n')
    file.close()

async def text_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log(update, context)
    msg = update.message.text
    items = [item for item in msg.split()]
    return items
    