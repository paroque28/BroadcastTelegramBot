import handlers.markup_keyboards as keyboards
import consts

def getRegex(markup_matrix):
    regex="^("
    for sublist in markup_matrix:
        for item in sublist:
            regex += item + "|"
    return regex[0:-1] + ")$"

main_regex = getRegex(keyboards.main_matrix)

if (consts.DEBUG == 2):
        print(main_regex)
