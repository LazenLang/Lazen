import info
import traceback
import text_utilities
import tokenizer
def tokenizer_optimize(token_list):
    # Basic Tokens Optimisations, Example : print(5 - -5) -> print(5-(0-5)) -> print(5+5)
    result = token_list
    return result
def optimize_plus_operator(i):
    line_result = []
    counter = 0
    x = 0
    for i2_raw in i:
        try:
            i2 = i[counter]
        except:
            break
        # Here we will optimize :
        """
        var
        +
        =
        12
        """
        # To :
        """
        var
        +=
        12
        """
        # And : print(5++ - 5) -> print((5+1) - 5)


        if i2 == "+":
            if i[counter + 1]:
                if i[counter + 1] == "+":
                    if not i[counter + 2]:
                        line_result.append("++")
                        counter += 1
                    elif i[counter + 2]:
                        if i[counter + 2] in info.tokenizing_symbols:
                            line_result.append("++")
                            counter += 1
                        else:
                            line_result.append("+")
                            line_result.append("+")
                            counter += 1
                else:
                    line_result.append("+")
            else:
                line_result.append("+")
        else:
            line_result.append(i2)
        counter += 1
    return line_result
