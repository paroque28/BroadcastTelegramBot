from telegram import ReplyKeyboardMarkup
import db
import consts as c

def getBestArrange(options):
    options = [options]
    rotate = [[options[j][i] for j in range(len(options))] for i in range(len(options[0]))] 
    if c.DEBUG == 2:
        print(options)
        print(rotate)
    return rotate

#MAIN
main_matrix = [['Suscribirme','Desuscribirme'],
               ['Dejar comentarios'],
               [ 'Información']]
main_markup = ReplyKeyboardMarkup(main_matrix, one_time_keyboard=True)


#SUBSCRIBE
subscribe_list = [sublist[1] for sublist in db.getSubscriptions()]
subscribe_matrix = getBestArrange(subscribe_list)
subscribe_markup = ReplyKeyboardMarkup(subscribe_matrix, one_time_keyboard=True)