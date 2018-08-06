import traceback
def list_to_str(list):
    result = ""
    for x in list:
        result += x
    return result
def str_to_list(str):
    result = []
    for x in str:
        result.append(x)
    return result
def erase_btwn_parn(input): # This function will erase the text between every parenthesis, including the parenthesis themselves.
                            # 'input' can be of  types String or List.
    result, opnd_parn, input_modificated = "", 0, []

    for x in input:
        for x2 in x:
            input_modificated.append(x2)

    for x in input_modificated:
        if x == "(":
            opnd_parn += 1
            result += " "
            continue
        elif x == ")":
            opnd_parn -= 1
            result += " "
            continue
        if not opnd_parn > 0:
            result += x
        else:
            result += " "
    return result

def erase_btwn_str(input): # This function will erase the text between every string literal,
                           # including the string literal symbols themselves.
    opened_str, result = False, ""
    for x in input:
        if x == "\"":
            if not opened_str: opened_str = True
            elif opened_str: opened_str = False
            continue
        if not opened_str:
            result += x
    return result

def repeat_char(char, times):
    result = ""
    for i in range(0, times):
        result += char
    return result

def check_if_type(input, type = "str"): # This function will check if 'input' is a Lazen string, char, numeric or letter.
    if input.strip() == "": return False
    if type == "str":
        if input.strip()[0] == "\"" and input.strip()[len(input.strip()) - 1] == "\""\
        and erase_btwn_str(input).strip() == "":
            return True
    elif type == "char":
        if input.strip()[0] == "\'" and input.strip()[len(input.strip()) - 1] == "\'" and len(input.strip()) == 3:
            return True
    elif type == "num":
        if is_int(input.strip()):
            return True
    elif type == "letter":
        if is_letter(input.strip()):
            return True
    return False

def remspaces_bn(input): # This function will remove every space at the beginning and the end of 'input'
    beginning, end = 0, 0
    for x in input:
        if x == " ": beginning += 1
        elif not x == " " and not x == "\t": break
    for x in reversed(input):
        if x == " ": end += 1
        elif not x == " " and not x == "\t": break
    return input[beginning : len(input) - end]

def bake_lit(input): # 'input' should be a token list, this function transforms a token_list containing raw literals
    """
    print
    (
    "
    a
    "
    )
    """
    # to ->
    """
    print
    (
    "a"
    )
    """
    opened_str, opened_char, result, build_str, build_char = False, False, [], "", ""

    for x in input:
        if opened_str and not x == "\"":
            build_str += x
            continue
        elif opened_char and not x == "\'":
            build_char += x
            continue

        if x == "\"":
            build_str += x
            if not opened_str: opened_str = True
            else:
                result.append(build_str)
                opened_str, build_str = False, ""
            continue
        elif x == "\'":
            build_char += x
            if not opened_char: opened_char = True
            else:
                result.append(build_char)
                opened_char, build_char = False, ""
            continue

        result.append(x)

    return result

def is_int(input):
    num_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for x in input:
        if not x in num_list:
            return False
    return True

def is_letter(input):
    letter_list = str_to_list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    if input in letter_list:
        return True
    else:
        return False

def remove_parn(input, return_type = "str"): # 'input' must be a list,
                                             # this function should remove the parenthesis
                                             # at the beginning and the end of the line.
    beg_sp_amount = 0
    # (5 + 5) | (5 + 5) * (6 + 1)
    try:
        if not count_char(input, "(") == count_char(input, ")"):
            if count_char(input, "(") > count_char(input, ")"):
                substract = count_char(input, "(") - count_char(input, ")")
                for x in repeat_char(")", substract):
                    input.append(x)
            else:
                substract = count_char(input, ")") - count_char(input, "(")
                for x in repeat_char("(", substract):
                    input.insert(0, x)

        for x in input:
            if x == "(":
                beg_sp_amount += 1
            else:
                break

        for i in range(0, beg_sp_amount):
            if erase_btwn_parn(input).strip() == "":
                input = input[1 : len(input) - 1]
            else:
                break
    except:
        pass

    if return_type == "lst":
        return input # 'input' should be a list,
                     # so, no need to convert it (to return it as a list).
    else:
        return list_to_str(input) # Here we convert 'input' (list) to String format.

def reverse_str(str):
    return list_to_str(reversed(str_to_list(str)))

def count_char(input, char): # This function returns the amount of the specified character occurences in the input.
                             # 'input' can be of types String or List.
    occurences = 0
    for x in input:
        if x == char:
            occurences += 1

    return occurences
#def remove_chars_and_strs(input): # This function will remove the text between every character and string declaration symbol,
                                  # including the symbol.

def check_if_contains(looking_for_char, list_or_string): # Python provides a "x in ..." to check if something contains something.
                                                        # But this function will return the index where the character you're looking
                                                         # for was found.
    if looking_for_char in list_or_string:
        return list_or_string.find(looking_for_char)

    return -1
