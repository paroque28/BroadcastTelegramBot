# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
import handlers.markup_keyboards as keyboards
import consts as c
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hola Bienvenido al bot de subscripciones TEC\n')
    update.message.reply_text('Que desea hacer?\n', reply_markup=keyboards.main_markup)
    return c.MAIN


def main(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('No implementado\n')
    update.message.reply_text('Que desea hacer?\n', reply_markup=keyboards.main_markup)
    return c.MAIN

def invalid_choice(update, context):
    update.message.reply_text('Opcion invalida\n')
    update.message.reply_text('Que desea hacer?\n',
        reply_markup=keyboards.main_markup)

def error(logger, update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def done(update, context):
    update.message.reply_text("Until next time!")
    return ConversationHandler.MAIN
