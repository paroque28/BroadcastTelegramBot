
from telegram.ext import (ConversationHandler, CommandHandler, MessageHandler, Filters)

from handlers import handlers, regex
import handlers.markup_keyboards as keyboards
import consts as c
import utils

# Add conversation handler with the states c.MAIN, c.SUBSCRIBE
conversation_handler = ConversationHandler(
    entry_points=[CommandHandler('start', handlers.start)],
    
    states={
        c.MAIN: [ MessageHandler( Filters.regex(regex.main_regex), handlers.main),],
        c.SUBSCRIBE: [ MessageHandler( Filters.regex(regex.subscribe_regex), handlers.subscribe),],
    },
    fallbacks=[MessageHandler( Filters.regex('^Done$'), handlers.done)],
    name="default_conversation",
    persistent=True
)
