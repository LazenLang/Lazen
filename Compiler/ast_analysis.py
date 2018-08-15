import text_utilities, errors

# This module processes semantic and syntaxic analysis on the abstract syntax tree.

declared_id = ["print", "if", "for", "while", "return", "else", "elif", "end", "true", "false", \
"str1", "str2", "str3", "int1", "int2", "int3"]

declared_id_types = ["function", "function", "function", "function", "function", "function", \
"function", "function", "bool", "bool", "str", "str", "str", "num", "num", "num"]

op_list = [",", "||", "&&", ":¨", "==", "§§", "&=", "!=", "<=", ">=", "+=", "/=", "*=", "-=", "^=", "%=" ,"=", ">", \
"<", "&", "+", "-", "%", "/", "*", "^", "@", "!"] # The Lazen operators list.
                                                  # Some aren't correct when used rawly on the source-code, as an example
                                                  # '@', '§§' and ':¨' are translated by the parser

def go(ast, line_n): # This function will return True or False, True == everything is ok,
                     # False == there is an error, it has been printed on the
                     # console ( Stop starting modules and just quit() if False)

    tab_amounts, tab_operators, op_lns = [], [], []

    op_elemc_lst = ["x|2", "x|2", "x|2", "1|", "x|2", "2|", "2|", "x|2", "x|2", "x|2", \
    "2|", "2|", "2|", "2|", "2|", "2|", "2|", "x|2", \
    "x|2", "x|2", "x|2", "x|2", "x|2", "x|2", "x|2", "x|2", "1/2|", "1|"]  # f_id here means the first child must be an identifier
                                                                           # x means unlimited amount of operands

    conct_op = ["+=", "-=", "/=", "*=", "^=", "%=", "&=", "="] # +=, -=, *=, &=, /=, ^=, %=, =, ...

    ####################################

    needed_types = ["any", "bool", "bool", "bool", "any", "any", "str/.any", "any", "num", "num", "num/.num", \
    "num/.num", "num/.num", "num/.num", "num/.num", "num/.num", "id.any", "num.num", "num.num", "str", "num", "num", \
    "num", "num", "num", "num", "id.any", "num"]

    # 'any' = any type
    # The '.' between two types means the first child must be ...
    # and the second child/all of the other children must be ...
    #
    # The '/' precises that the element must be an identifier.

    ####################################


    needed_types_precise = [""]


    for counter, x in enumerate(ast.split("\n")):
        if x.replace("\t", "") in op_list:
            #print("op: ", x.replace("\t", ""))
            tab_operators.append(x.replace("\t", ""))   # Here we append x (the operator) to the list 'tab_operators'.
            op_lns.append(counter)  # We append the line where x (the operator) was encountered, in the same array as in tab_operators.

            tab_amounts.append(text_utilities.count_chars_bg(x, "\t") + 1) # We append the tab amount before x (the operator)
                                                                           # to the list 'tab_amounts'.

    for counter, x in enumerate(tab_operators): # We're browsing into tab_operators.
        children, elemc_splt = get_children(x, ast, op_lns[counter], tab_amounts[counter]), op_elemc_lst[op_list.index(x)].split("|")

        # Below we're doing some basic AST analysis (also known as 'parsing', but it is just analysis there).
        # Here we're checking if each operator made to modify a variable is correctly used if it is in the line.

        if len(ast.split("\n")) > 0:
            for x2 in conct_op:
                if x2 in tab_operators and not ast.split("\n")[0].strip() == x2: errors.pup_error(errors.get_error("0019", [x2, line_n]))


        # Directly below this comment we're doing analysis on the amount of children that each operator must have.

        if elemc_splt[0] == "x":
            if elemc_splt[1] != "":

                if not len(children) >= int(elemc_splt[1]): errors.pup_error(errors.get_error("0010",\
                [elemc_splt[1], x, len(children), line_n]))

        elif elemc_splt[0] == "2" or elemc_splt[0] == "1":

            if len(children) != int(elemc_splt[0]): errors.pup_error(errors.get_error("0011",\
            [elemc_splt[0], x, len(children), line_n]))

        elif "/" in elemc_splt[0]:
            fnd_one, splt_slsh = False, elemc_splt[0].split("/")
            for x2 in splt_slsh:
                if len(children) == int(x2):
                    fnd_one = True
                    break

            if not fnd_one: errors.pup_error(errors.get_error("0012", [splt_slsh[0], splt_slsh[1], x, len(children), line_n]))


    # Now we're going to analyze each element on the AST and check if it's a valid element.

    for counter, x in enumerate(ast.split("\n")):
        getType = text_utilities.get_type(x.replace("\t", ""))

        if getType == "id":
            if not x.strip().lower() in declared_id: errors.pup_error(errors.get_error("0014", [x.strip(), line_n]))
            pass # This is temporary, so I just have to delete the line above when I don't want the
                 # analyzer to check if each identifier exists.

        elif getType == "unk":

            if x.strip().startswith("'") and x.strip().endswith("'") and not len(x) in range(2,4):
                errors.pup_error(errors.get_error("0015", [x.strip(), line_n]))

            elif len(x.strip()) > 0:
                if x.strip()[0].isdigit(): errors.pup_error(errors.get_error("0017", [x.strip(), line_n]))


            errors.pup_error(errors.get_error("0016", [x.strip(), line_n]))


    # Now we're doing some basic types analysis #

    for counter, x in enumerate(tab_operators):
        children, true_false, idx_oplst = get_children(x, ast, op_lns[counter], tab_amounts[counter]), ["true", "false"], op_list.index(x)
        if counter == 0 and x == "=" and children[0].lower() in true_false: errors.pup_error(errors.get_error("0020", [children[0], line_n]))
        ndd_types = needed_types[idx_oplst]

        if "." in ndd_types:
            splt_point, operand_num = ndd_types.split("."), 1

            if splt_point[0].endswith("/") and not text_utilities.check_type_okop(children[0], "id"):

                errors.pup_error(errors.get_error("0021", [children[0], x, line_n,\
                splt_point[0].replace("/", " identifier"),\
                text_utilities.get_type(children[0])]))

            if not text_utilities.check_type_okop(children[0], splt_point[0]) or not \
            text_utilities.check_type_okop(children[1], splt_point[1]):

                if not text_utilities.check_type_okop(children[0], splt_point[0]): operand_num = 0

                errors.pup_error(errors.get_error("0021",\
                [children[operand_num], x, line_n, splt_point[operand_num].replace("/",""),\
                text_utilities.get_type(children[operand_num])]))

            pass

        elif ndd_types != "any":
            for x2 in children:
                g_type = text_utilities.get_type(x2)
                if g_type != ndd_types: errors.pup_error(errors.get_error("0021",\
                [x2, x, line_n, ndd_types, g_type]))
                pass

        if x == "@" and text_utilities.get_type(children[0]) != "function": errors.pup_error(\
        errors.get_error("0022", [children[0], line_n]))

    return True

def get_children(operator, ps_res, ps_line, tab_amount): # This function will return the amount of children
                                                         # of the specified operator on the abstract syntax tree.
    result, children = "", []
    for x in ps_res.split("\n")[ps_line+1 : len(ps_res.split("\n"))]:
        if text_utilities.count_chars_bg(x, "\t") < tab_amount: break
        if text_utilities.count_chars_bg(x, "\t") == tab_amount: children.append(x.strip())
    return children
