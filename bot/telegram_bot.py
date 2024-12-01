from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
)

async def start(update: Update, context):
    await update.message.reply_text("Welcome to sportlife bot!")

async def handle_message(update: Update, context):
    user_id = update.message.chat.id
    text = update.message.text

    # Make API request (example)
    import requests
    requests.post(
        'http://127.0.0.1:8000/bot/create/',
        json={'user_id': user_id, 'message_text': text}
    )

    await update.message.reply_text("Your message has been saved!")

def main():
    application = Application.builder().token("7530359381:AAFjFtTjg5YGciOPcuTQtXmA8QCvzWlXUaQ").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()

if __name__ == "__main__":
    main()
