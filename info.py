def build_straight_ln():
    return "\n\n-------------------------------------------------\n"


# Variable declarations #

help = build_straight_ln() + """\n\n'--file' argument : Specify the code-file to interpret.
'--help' argument : Show the command-line help.
'--version' argument : Show the current installed Lazen version on this machine.""" + build_straight_ln()

version = "1.0"

tokenizing_symbols = ["(", ")", "\"", "\'", "-", "+", \
"/", "^", "*", "%", ";", ",", "&", "<", ">", "=", "!", \
".", "}", "{", "/", " "]

# --------------------- #
