#
#
#TODOs:
#   Add header to all files!
#   Based on https://github.com/python-telegram-bot/python-telegram-bot/blob/master/examples/persistentconversationbot.py
#   Add license in headers

'''
By:
    Pablo Rodriguez Quesada
    Abraham Arias Chinchilla
Freb. 2019
'''

import os
import logging
from pathlib import Path

from telegram.ext import (Updater, PicklePersistence, ConversationHandler, CommandHandler)

from handlers import handlers
import states, utils

#from telegram import ReplyKeyboardMarkup
#from telegram.ext import (MessageHandler, Filters)
#import db
#import logging
#from threading import Thread
#from time import sleep
#from datetime import datetime
#from pytz import timezone

VERSION = 1.0
HOME = str(Path.home())
TOKEN = "186503385:AAE46-96rYTLWhEUmXYD6cjJQv1FOe1r5VY" #os.environ['TELEGRAM_TOKEN']

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

persistence = PicklePersistence(filename=HOME+'/telegram/save_state')
bot = None


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)

def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(TOKEN, persistence=persistence, use_context=True)
    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    dp.add_handler(states.conv_handler)

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()
    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
