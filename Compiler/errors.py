import info, text_utilities, time, start_modules

def get_error(id, providedinfo = []):
    if id == "0001":
        return "File-path expected after '--file' argument."

    elif id == "0002":
        return "Unable to read the file '" + str(providedinfo[0]) + "'."

    elif id == "0003":
        return "Incorrect symbol repetition (line: " + str(providedinfo[0]) + ", col: " + str(providedinfo[2]) + ").\n" \
        "Additional Information : Symbol '" + providedinfo[1] + "' were repeated where it shouldn't be."

    elif id == "0004":
        return "Unclosed Char literal. Excepted (') after each ('). (line: " + str(providedinfo[0]) + ")\n" \
        "Example : print('a') -> valid, print('a) -> invalid."

    elif id == "0005":
        return "Unclosed String literal. Excepted (\") after each (\"). (line: " + str(providedinfo[0]) + ")\n" \
        "Example : print(\"text\") -> valid, print(\"text) -> invalid."

    elif id == "0006":
        return "Unclosed Parenthesis. Expected ')' after each '('. (line: " + str(providedinfo[0]) + ")\n" \
        "Example : x(a(5) * 5) -> valid, x(a(5 * 5) -> invalid."

    elif id == "0007":
        return "Unnecessary closing parenthesis. Expected '(' before each ')'. (line: " + str(providedinfo[0]) + ")\n" \
        "Example : x(a(5) * 5) -> valid, x(a(5) * 5)) -> invalid."

    elif id == "0008":
        return "Invalid character '" + str(providedinfo[0]) + "' (line: " +\
        str(providedinfo[1]) +", col: " + str(providedinfo[2]) + ")\n"
        "Example : x(5 + 5) -> valid, x(" + providedinfo[0] + "5 + 5) -> invalid."

    elif id == "0009":
        return "Incorrect symbol repetition (line: " + str(providedinfo[0]) + ", col: " + str(int(providedinfo[2]) + 3) + ").\n" \
        "Additional Information : Symbol '" + providedinfo[1] + "' were repeated where it shouldn't be.\n" \
        "This symbol is a minus or plus operator; it means it can be repeated 3 times maximum."

    elif id == "0010":
        return "Expected " + str(providedinfo[0]) + " or more value(s) for operator '" + \
        str(providedinfo[1]) + "' where only \n" + str(providedinfo[2]) + " value(s) were provided. \
        (line: " + str(providedinfo[3]) + ")\n" + "\nExample : x(5%4.25) -> valid, x(5%) -> invalid."

    elif id == "0011":
        return "Expected " + str(providedinfo[0]) + " value(s) for operator '" + providedinfo[1] +\
        "' where " + str(providedinfo[2]) +" value(s) were provided. (line: " + str(providedinfo[3]) + ")"

    elif id == "0012":
        return "Expected " + str(providedinfo[0]) + " or " + str(providedinfo[1]) + " values for operator '" + \
        str(providedinfo[2]) + "' where " + str(providedinfo[3]) + " value(s) were provided. (line: " +\
        str(providedinfo[4]) + ")"

    elif id == "0013":
        return "Syntax Error (line: " + str(providedinfo[0]) + ", col: " + str(providedinfo[1])+ ")\n" \
        "Additional Information : " + providedinfo[2]

    elif id == "0014":
        return "Unknown/undeclared identifier '" + str(providedinfo[0]) + "'. (line: " + str(providedinfo[1]) + ")\n" \
        "Example : print(lxk) -> invalid because 'lxk' is not known or declared yet in the source-code."

    elif id == "0015":
        return "Invalid char literal " + str(providedinfo[0]) + ". (line: " + str(providedinfo[1]) + ")\n" \
        "Example : print('a') -> valid, print('abc') -> invalid."

    elif id == "0016":
        return "Unknown type for '" + str(providedinfo[0]) + "' (line: " + str(providedinfo[1]) + ")."

    elif id == "0017":
        return "Invalid identifier '" + str(providedinfo[0]) + "'. \
An identifier cannot start with a digit. (line: " + str(providedinfo[1]) + ")\n"\
        "Example : print(tcx4) -> valid, print(4tcx) -> invalid."

    elif id == "0018":
        # This error message is temporarily removed.
        pass

    elif id == "0019":
        return "Invalid usage of operator '" + str(providedinfo[0]) + "'. (line: " + str(providedinfo[1]) + ")\n" \
        "Example : print(foo " + str(providedinfo[0]) + " 5) -> invalid, foo " + str(providedinfo[0]) + " 5 -> valid.\n\n" \
        "Tip : If an operator made to modify a variable is used in a line, it must be the first operator used in the line."

    elif id == "0020":
        return "Invalid variable name '" + str(providedinfo[0]) + "'. (line: " + str(providedinfo[1]) + ")\n" \
        "Additional Information : A variable name can't be a boolean identifier (true or false)."

    elif id == "0021":
        return "Operand '" + str(providedinfo[0]) + "' has an invalid type for operator '" + \
        str(providedinfo[1]) + "'. (line: " + str(providedinfo[2]) + ")\n" \
        "Additional Information : Excepted '" + str(providedinfo[3]) + "' type, got '" + str(providedinfo[4]) + "' type."

    elif id == "0022":
        return "Undefined function '" + str(providedinfo[0]) + "' (line: " + str(providedinfo[1]) + ").\n" \
        "Example : print(\"some text\") -> valid, xarl(42) -> invalid because function 'xarl' is not defined as a function."
def pup_error(message):
    t1 = time.clock()
    print(info.bcolors.FAIL + "Compilation aborted after " +  str(t1 - start_modules.t0) + " seconds." + info.bcolors.ENDC)

    print("\n\t      " + info.bcolors.WARNING + "An error occured" +\
    info.bcolors.ENDC + "\n--------------------------------------------\n")
    print(message)
    print("\n--------------------------------------------\n")

    quit()

def bsc_syntx_errs(token_list, line_n, invl_symb = False): # The provided token list should be an optimized token list
                                                           # if invl symb is False. This function will check for basic
                                                           # minor syntaxic errors on the line.

    if invl_symb:
        symb_white, count_col = info.tokenizing_symbols + ["_", "\\", "\t"], 0

        for x in token_list:
            count_col += len(x)

            if not text_utilities.check_if_type(x, "char") and not \
            text_utilities.check_if_type(x, "str") and not \
            text_utilities.check_if_type(x, "num") and not text_utilities.check_if_type(x, "letter"):

                for counter, browse_in in enumerate(x):
                    if not browse_in in symb_white and not text_utilities.check_if_type(browse_in, "num") \
                    and not text_utilities.check_if_type(browse_in, "letter"):
                        column = count_col
                        if not counter == len(x): column == count_col - (len(x) - counter)
                        pup_error(get_error("0008", [browse_in, line_n, column]))
                        return

    g_bfr, colcnt = "", 0
    symb_black = [";", ".", "!"]  # Symbols to prevent from repeating in the code

    for counter, x in enumerate(token_list):

        if g_bfr == x and x in symb_black:
            pup_error(get_error("0003", [line_n, x, colcnt + 2]))

        if x == ")":
            if g_bfr in info.operators and not g_bfr == "!" or g_bfr == ".":
                colcnt += len(x)
                pup_error(get_error("0013", [line_n, colcnt, "Symbol/operator is followed by a closing parenthesis."]))

        elif x in info.operators and not x == "!" and counter == len(token_list)-1:
            colcnt += len(x)
            pup_error(get_error("0013", [line_n, colcnt, "Code line is ending with a symbol/operator."]))

        colcnt += len(x)
        g_bfr = str(x)

    if len(token_list) >= 1:
        if token_list[0] in info.operators:
            pup_error(get_error("0013", [line_n, 0, "Code line is starting with a symbol/operator."]))

def unclosed_symbols_verification(code):
    line_counter = 0
    for i in code.split("\n"):
        opened_str = False
        opened_char = False
        opened_parenthesis = 0
        for i2 in i:
            if opened_str and not i2 == "\"":
                    continue
            elif opened_char and not i2 == "\'":
                    continue

            if i2 == "\"":
                if not opened_str:
                    opened_str = True
                else:
                    opened_str = False
            elif i2 == "\'":
                if not opened_char:
                    opened_char = True
                else:
                    opened_char = False
            elif i2 == "(":
                opened_parenthesis += 1
            elif i2 == ")":
                opened_parenthesis -= 1
        if opened_str or opened_char or opened_parenthesis:
            if opened_str:
                return [False, "str", line_counter]
            elif opened_char:
                return [False, "char", line_counter]
            elif opened_parenthesis > 0:
                return [False, "tmop", line_counter]
            elif opened_parenthesis < 0:
                return [False, "tmcp", line_counter]
        line_counter += 1
    return [True]
