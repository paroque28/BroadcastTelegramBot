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
    text = update.message.text
    #Subscribe
    if (text == keyboards.main_matrix[0][0]):
        update.message.reply_text('Tenemos disponible las siguientes suscripciones:\n1. Memes\n 2.Comedor\n')
        update.message.reply_text('A cual se desea suscribir?\n', reply_markup=keyboards.subscribe_markup)
        return c.SUBSCRIBE
    update.message.reply_text('No implementado\n')
    update.message.reply_text('Que desea hacer?\n', reply_markup=keyboards.main_markup)
    return c.MAIN

def subscribe(update, context):
    """ Subscribe menu """
    text = update.message.text
    if (c.DEBUG == 2):
        print("Selecciono: "+ text)
    update.message.reply_text('Ud seleccionó: '+ text + "\nAún no se puede suscribir!\n")
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
