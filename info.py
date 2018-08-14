def build_straight_ln():
    return "\n\n-------------------------------------------------\n"


# Variable declarations #

help = build_straight_ln() + """\n\n'--file' argument : Specify the code-file to interpret.
'--help' argument : Show the command-line help.
'--version' argument : Show the current installed Lazen version on this machine.""" + build_straight_ln()

version = "1.0"

tokenizing_symbols = ["(", ")", "\"", "\'", "-", "+", \
"/", "^", "*", "%", ";", ",", "&", "<", ">", "=", "!", \
".", "}", "{", " ", "#"]

operators = ["+", "-", "*", "/", "^", "%", ";", ",", "<", \
">", "=", "!"]

parsing_symbols = [",", "||", "&&", ":¨", "==", "§§", "&=", "!=", "<=", ">=", "+=", "/=", "*=", "-=", "^=", "%=" ,"=", ">", \
"<", "&", "^", "*", "/", "%", "-", "+", "@", "!"]

# --------------------- #

########################################### SOURCE ##########################################

# joeld, eryksun (https://stackoverflow.com/a/287944) #

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#############################################################################################"
