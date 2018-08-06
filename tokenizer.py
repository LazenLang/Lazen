import info
import errors
import text_utilities
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

    # Invalid Symbols Verification (fast) #
    symb_white, count_col = info.tokenizing_symbols + ["_", "\\"], 0

    for cc in line_result_copy_1:
        count_col += len(cc)
        if not text_utilities.check_if_type(cc, "char") and not text_utilities.check_if_type(cc, "str") and not text_utilities.check_if_type(cc, "num") \
        and not text_utilities.check_if_type(cc, "letter"):
            for counter, browse_in in enumerate(cc):
                if not browse_in in symb_white and not text_utilities.check_if_type(browse_in, "num") \
                and not text_utilities.check_if_type(browse_in, "letter"):
                    column = count_col
                    if not counter == len(cc):
                        column == count_col - (len(cc) - counter)
                    errors.pup_error(errors.get_error("0008", browse_in, str(line_counter + 2), str(column - 1)))

    # Symbols-Repetition Verification (fast) #

    ch_counter, last_symb, symb_black = 0, "", [";", "&", "<", ">", "*", "^", "/", "%", ".", "!", "{", "}"] # Symbols to prevent from repeating in the code

    for i10 in line_result_copy_1:
        if last_symb == i10 and i10 in symb_black:
            errors.pup_error(errors.get_error("0003", str(line_counter + 2), i10, str(ch_counter)))
        ch_counter += len(i10)
        last_symb = i10

    # Now we're going to prevent some other symbols to repeat more than ... times (can exceed 2 times for verification)

    """
    Maximal repetitions amount for each operator

    + : 4 times
    - : 4 times

    """

    last_four_symb, temp_list, col_cnter = [], [], 0


    for x in line_result_copy_1:
        col_cnter += len(x)
        if not x in last_four_symb:
            for x2 in last_four_symb:
                temp_list.append(x2)
            last_four_symb.clear()
        last_four_symb.append(x)
        if len(last_four_symb) >= 4:
            symb_olist = last_four_symb[0]
            if symb_olist == "+" or symb_olist == "-":
                errors.pup_error(errors.get_error("0009", str(line_counter + 2), symb_olist, str(col_cnter - 3)))
                continue
        temp_list.append(x)

    """
    Ajouter les opérateurs à double-signe,
    exemples : ==, !=, <=, >=, +=,
    /=, *=, -=, ^=, %=,

    Fixer l'optimisateur. (facultatif, peut être fait plus tard)

    Gérer les fonctions dans les expressions.
    """
    #####################################################
    try:
        if line_result_copy_1[len(line_result_copy_1) - 1] == ";": # Detects and remove an eventually existing semicolon at the end of the line.
            line_result_copy_1.pop(len(line_result_copy_1) - 1) #
    except:
        pass
    return line_result_copy_1

def go(code, return_w_spces = False):
    result = []
    line_counter = -1
    for i in code.split("\n"):
        _tokenizeLn = tokenize_line(i, line_counter, return_w_spces, False)
        line_counter += 1
        result.append(_tokenizeLn);
    return result
