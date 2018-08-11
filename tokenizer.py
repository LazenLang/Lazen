import info, errors, text_utilities
def tokenize_line(line, line_counter, return_w_spces, return_raw = False):
    line_result_raw = []
    line_result = []
    adder = 0
    counter = -1
    line += "."

    for i2 in line:
        counter += 1
        if i2 in info.tokenizing_symbols:
            line_result_raw.append(line[adder : counter])
            line_result_raw.append(i2)
            adder = counter + 1

    line_result_raw.pop()

    if return_raw:
        return line_result_raw

    opened_str, opened_char = False, False
    build_str, build_char = "", ""
    i3_counter = 0

    for i3 in line_result_raw:
        if opened_str:
            if not i3 == "\"":
                build_str += i3
                continue
        if opened_char:
            if not i3 == "\'":
                build_char += i3
                continue
        if not opened_str and not opened_char and not i3 == "\"" and not i3 == "\'":
            line_result.append(i3)

        if i3 == "\"":
            if not opened_str:
                build_str += i3
                opened_str = True
            else:
                build_str += i3
                line_result.append(build_str)
                build_str = ""
                opened_str = False
        elif i3 == "\'":
            if not opened_char:
                build_char += i3
                opened_char = True
            else:
                build_char += i3
                line_result.append(build_char)
                build_char = ""
                opened_char = False

    line_result_copy, line_result_copy_1, line_result_final = [],[],[]
    counter_1, x, precedent_i8 = 0, 0, ""

    for i8 in line_result:
        if not return_w_spces:
            if not i8.strip() == "":
                line_result_copy.append(i8.strip())
        else:
            if i8 == " " or not i8 == "":
                line_result_copy.append(i8)

    # Removes end-line comments #

    for counter, i9 in enumerate(line_result_copy):
        if i9 == "#":
            break
        line_result_copy_1.append(i9)

    ###################################

    try:
        if line_result_copy_1[len(line_result_copy_1) - 1] == ";": # Detects and remove an eventually existing semicolon at the end of the line.
            line_result_copy_1.pop(len(line_result_copy_1) - 1) #
    except:
        pass

    return line_result_copy_1

def go(code, ret_w_spces = False):
    result = []
    line_counter = -1

    for i in code.split("\n"):
        _tokenizeLn = tokenize_line(i, line_counter, ret_w_spces, False)
        line_counter += 1
        result.append(_tokenizeLn);

    return result
