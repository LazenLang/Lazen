def get_error(id, providedinfo = "", providedinfo2 = "", providedinfo3 = ""):
    if id == "0001":
        return "File-path expected after '--file' argument."
    elif id == "0002":
        return "Unable to read the file '" + providedinfo + "'."
    elif id == "0003":
        return "Incorrect symbol repetition (line: " + providedinfo + ", col: " + providedinfo3 + ").\n" \
        "Additional Information : Symbol '" + providedinfo2 + "' were repeated where it shouldn't be."
    elif id == "0004":
        return "Unclosed Char literal. Excepted (') after each ('). (line: " + providedinfo + ")\n" \
        "Additional Information : print('a') -> valid, print('a) -> unvalid."
    elif id == "0005":
        return "Unclosed String literal. Excepted (\") after each (\"). (line: " + providedinfo + ")\n" \
        "Additional Information : print(\"text\") -> valid, print(\"text) -> unvalid."
    elif id == "0006":
        return "Unclosed Parenthesis. Expected ')' after each '('. (line: " + providedinfo + ")\n" \
        "Additional Information : x(a(5) * 5) -> valid, x(a(5 * 5) -> unvalid."
    elif id == "0007":
        return "Unnecessary closing parenthesis. Expected '(' before each ')'. (line: " + providedinfo + ")\n" \
        "Additional Information : x(a(5) * 5) -> valid, x(a(5) * 5)) -> unvalid."
    elif id == "0008":
        return "Invalid character '" + providedinfo + "' (line: " + providedinfo2 +", col: " + providedinfo3 + ")\n" \
        "Additional Information : x(5 + 5) -> valid, x(" + providedinfo + "5 + 5) -> unvalid."
    elif id == "0009":
        return "Incorrect symbol repetition (line: " + providedinfo + ", col: " + str(int(providedinfo3) + 3) + ").\n" \
        "Additional Information : Symbol '" + providedinfo2 + "' were repeated where it shouldn't be.\n" \
        "This symbol is a minus or plus operator; it means it can be repeated 3 times maximum."
def pup_error(message):
    print(message)
    quit()
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
