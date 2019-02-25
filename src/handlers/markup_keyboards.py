from telegram import ReplyKeyboardMarkup

main_matrix = [['Suscribirme','Desuscribirme'],
               ['Dejar comentarios'],
               [ 'Información']]
main_markup = ReplyKeyboardMarkup(main_matrix, one_time_keyboard=True)

subscribe_matrix = [['Memes','Comedor'],]
subscribe_markup = ReplyKeyboardMarkup(subscribe_matrix, one_time_keyboard=True)