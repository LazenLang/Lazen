import text_utilities
import errors

# This module processes semantic and syntaxic analysis on the abstract syntax tree.

declared_id = ["print", "if", "for", "while", "return", "else", "elif", "var1", "var2", "var3"]

op_list = [",", "||", "&&", ":¨", "==", "§§", "&=", "!=", "<=", ">=", "+=", "/=", "*=", "-=", "^=", "%=" ,"=", ">", \
"<", "&", "+", "-", "%", "/", "*", "^", "@", "!"] # The Lazen operators list.
                                                  # Some aren't correct when used rawly on the source-code, as an example
                                                  # '@', '§§' and ':¨' are translated by the parser

def go(ast, line_n): # This function will return True or False, True == everything is ok,
                     # False == there is an error, it has been printed on the
                     # console ( Stop starting modules and just quit() if False)

    tab_amounts, tab_operators, op_lns = [], [], []
    op_elemc_lst = ["x|2", "x|2", "x|2", "1|", "x|2", "2|", "2|f_id", "x|2", "x|2", "x|2",\
    "2|f_id", "2|f_id", "2|f_id", "2|f_id", "2|f_id", "2|f_id", "2|", "x|2",\
    "x|2", "x|2", "x|2", "x|2", "x|2", "x|2", "x|2", "x|2", "1/2|", "1|"]  # f_id here means the first child must be an identifier

    for counter, x in enumerate(ast.split("\n")):
        if x.replace("\t", "") in op_list:

            tab_operators.append(x.replace("\t", ""))   # Here we append x (the operator) to the list 'tab_operators'.
            op_lns.append(counter)  # We append the line where x (the ope  rator) was encountered, in the same array as in tab_operators.

            tab_amounts.append(text_utilities.count_chars_bg(x, "\t") + 1) # We append the tab amount before x (the operator)
                                                                           # to the list 'tab_amounts'.

    for counter, x in enumerate(tab_operators): # We're browsing into tab_operators.
        children, elemc_splt = get_children(x, ast, op_lns[counter], tab_amounts[counter]), op_elemc_lst[op_list.index(x)].split("|")
        print("operator: ", x, " with line ", op_lns[counter] , "/ children amount: ", len(children))

        # Below we're doing some basic AST analysis (also known as 'parsing', but it is just analysis there),
        # directly below this comment we're doing analysis on the amount of children that each operator must have.

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

        if elemc_splt[1] == "f_id":
            if not text_utilities.get_type(children[0]) == "id": errors.pup_error(errors.get_error(\
            "0018", [children[0], x, line_n]))

        ###################################################################################################


    # Now we're going to analyze each element on the AST and check if it's a valid element.
    # (example: does this identifier exists ?)

    for counter, x in enumerate(ast.split("\n")):
        getType = text_utilities.get_type(x.replace("\t", ""))

        if getType == "id":
            if not x.strip().lower() in declared_id: errors.pup_error(errors.get_error("0014", [x.strip(), line_n]))
            pass # This is temporary, so i just have to delete the line above when i don't want the
                 # analyzer to check if each identifier exists.

        elif getType == "unk":

            if x.strip().startswith("'") and x.strip().endswith("'") and not len(x) in range(2,4):
                errors.pup_error(errors.get_error("0015", [x.strip(), line_n]))

            elif len(x.strip()) > 0:
                if x.strip()[0].isdigit(): errors.pup_error(errors.get_error("0017", [x.strip(), line_n]))


            errors.pup_error(errors.get_error("0016", [x.strip(), line_n]))

    ###########################################################################################

    return True

def get_children(operator, ps_res, ps_line, tab_amount): # This function will return the amount of children
                                                         # of the specified operator on the abstract syntax tree.
    result, children = "", []
    for x in ps_res.split("\n")[ps_line+1 : len(ps_res.split("\n"))]:
        if text_utilities.count_chars_bg(x, "\t") < tab_amount: break
        if text_utilities.count_chars_bg(x, "\t") == tab_amount: children.append(x.strip())
    return children
