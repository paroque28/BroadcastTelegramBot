
from telegram import ReplyKeyboardMarkup
from telegram.ext import (ConversationHandler, CommandHandler, MessageHandler, Filters)

from handlers import handlers
import utils

reply_keyboard = [['Age', 'Favourite colour'],
                  ['Number of siblings', 'Something else...'],
                  ['Done']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)

# Add conversation handler with the states CHOOSING, TYPING_CHOICE and TYPING_REPLY
CHOOSING, TYPING_REPLY, TYPING_CHOICE = range(3)

def regular_choice(update, context):
    text = update.message.text
    context.user_data['choice'] = text
    if context.user_data.get(text):
        reply_text = 'Your {}, I already know the following ' \
                     'about that: {}'.format(text.lower(), context.user_data[text.lower()])
    else:
        reply_text = 'Your {}? Yes, I would love to hear about that!'.format(text.lower())
    update.message.reply_text(reply_text)
    return TYPING_REPLY


def custom_choice(update, context):
    update.message.reply_text('Alright, please send me the category first, '
                              'for example "Most impressive skill"')
    return TYPING_CHOICE

def received_information(update, context):
    text = update.message.text
    category = context.user_data['choice']
    context.user_data[category] = text.lower()
    del context.user_data['choice']

    update.message.reply_text("Neat! Just so you know, this is what you already told me:"
                              "{}"
                              "You can tell me more, or change your opinion on "
                              "something.".format(utils.facts_to_str(context.user_data)),
                              reply_markup=markup)

    return CHOOSING

def done(update, context):
    if 'choice' in context.user_data:
        del context.user_data['choice']

    update.message.reply_text("I learned these facts about you:"
                              "{}"
                              "Until next time!".format(utils.facts_to_str(context.user_data)))
    return ConversationHandler.END


# Add conversation handler with the states c.MAIN, c.SUBSCRIBE
conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', handlers.start)],
    
    states={
        CHOOSING: [MessageHandler( Filters.regex('^(Age|Favourite colour|Number of siblings)$'),
                                regular_choice),
                   MessageHandler( Filters.regex('^Something else...$'),
                                custom_choice),
                   ],
        TYPING_CHOICE: [MessageHandler(Filters.text, 
                                       regular_choice),
                        ],
        TYPING_REPLY: [MessageHandler(Filters.text,
                                      received_information),
                      ],
    },
    fallbacks=[MessageHandler( Filters.regex('^Done$'), done)],
    name="my_conversation",
    persistent=True
)
