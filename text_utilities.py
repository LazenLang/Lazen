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
    result = ""
    opnd_parn = False
    for x in input:
        if x == "(":
            opnd_parn = True
            result += " "
            continue
        elif x == ")":
            opnd_parn = False
            result += " "
            continue
        if not opnd_parn:
            result += x
        else:
            result += " "
    return result

def remove_parn(input): # 'input' must be a string, this function should remove the parenthesis at the beginning and the end of the line.
    beg_sp_amount = 0
    # (5 + 5) | (5 + 5) * (6 + 1)

    if not input.strip().startswith("(") and not input.strip().endswith(")"):
        return input

    if erase_btwn_parn(input).strip() == "":
        print("input: ", input, " / choice: 1")
        for x in input.strip():
            if x == "(":
                beg_sp_amount += 1
            else:
                break
        for i in range(0, beg_sp_amount):
            input = input[1 : len(input) - 1]
    else:
        print("input: ", input, " / choice: 2")
    return input
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
    for counter,x in enumerate(list_or_string):
        if x == looking_for_char:
            return counter

    return -1
