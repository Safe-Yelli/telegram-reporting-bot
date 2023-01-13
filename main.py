import os

from telegram import Update  #upm package(python-telegram-bot)
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext  #upm package(python-telegram-bot)


def help_command(update: Update, context: CallbackContext) -> None:
    text = '''testing for safeyelli.in'''
    update.message.reply_text(text)


def receive_location(update, context):
    current_pos = (update.message.location.latitude, update.message.location.longitude)
    print(current_pos)

def main():
    updater = Updater(os.getenv("token"))

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", help_command))
    location_handler = MessageHandler(Filters.location, receive_location)
    dispatcher.add_handler(location_handler)

    updater.start_polling()
    updater.idle()
  
if __name__ == '__main__':
    main()
