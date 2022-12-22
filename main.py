import emoji
import matplotlib
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import bot_commands

app = ApplicationBuilder().token("5989368249:AAGVyWQLA5B9W5moVNh_vbsY40jvk01BY6g").build()

app.add_handler(CommandHandler("Hi", bot_commands.hi_command))
app.add_handler(CommandHandler("time", bot_commands.time_command))
app.add_handler(CommandHandler("sum", bot_commands.sum_command))

print('server start')
app.run_polling()
