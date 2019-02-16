from telegram import ReplyKeyboardMarkup
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler, PicklePersistence)
import db
import logging
from pathlib import Path
from threading import Thread
from time import sleep
from datetime import datetime
from pytz import timezone

VERSION = 1.0
HOME = str(Path.home())
TOKEN = os.environ['TELEGRAM_TOKEN']

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
persistence = PicklePersistence(filename=HOME+'/telegram/save_state')
bot = None

def main():
    global bot
    #Read Token
    token = someVariable = os.environ['TELEGRAM_TOKEN']
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(token, persistence=persistence)
    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    bot = dp.bot
    # Add conversation handler with the states c.MAIN, c.SUBSCRIBE
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            c.MAIN: [RegexHandler('^(Accion1|Accion2)$',
                                    main_menu,
                                    pass_user_data=True),
                       ],
        },

        fallbacks=[RegexHandler('^Done$', done, pass_user_data=True)],
        persistent=True, name='default'
    )

    dp.add_handler(conv_handler)

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