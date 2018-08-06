import info
import traceback
import text_utilities
import tokenizer
def tokenizer_optimize(token_list, first_time = False):
    # Basic Tokens Optimisations, Examples -
    # +1 -> 1 | +(1+1) -> (1+1)
    # -1 -> (0-1) | -(5+5) -> (0-(5+5))
    # 1++ -> (1+1) | (1+5)++ -> ((1+5)+1)

    result, counter_impact, break_end = [], 0, False

    for counter in range(0, len(token_list)):
        if counter_impact > len(token_list)-1: break
        get_after, x = "", token_list[counter_impact]

        try:
            get_after = token_list[counter_impact + 1]
        except:
            break_end = True

        if first_time and not x in info.tokenizing_symbols and not get_after in info.tokenizing_symbols and counter == 0:
            result.append(x)
            result.append("$")
            result.append("(")
            for x2 in token_list[counter_impact + 1 : len(token_list)]:
                result.append(x2)
            result.append(")")
            break

        if x == "!" and get_after == "=": result.append("!=")

        elif x == "=" and get_after == "=": result.append("==")
        elif x == "<" and get_after == "=": result.append("<=")
        elif x == ">" and get_after == "=": result.append(">=")
        elif x == "+" and get_after == "=": result.append("+=")
        elif x == "-" and get_after == "=": result.append("-=")
        elif x == "/" and get_after == "=": result.append("/=")
        elif x == "*" and get_after == "=": result.append("*=")
        elif x == "^" and get_after == "=": result.append("^=")
        elif x == "%" and get_after == "=": result.append("%=")
        elif x == "&" and get_after == "=": result.append("&=")
        elif x == "&" and get_after == "&": result.append("&&")
        elif x.lower() == "and":
            counter_impact -= 1
            result.append("&&")

        elif not x in info.tokenizing_symbols and not x == "@" and not x == "$" and get_after == "(":
            counter_impact -= 1
            result.append(x)
            result.append("@")
        else:
            counter_impact -= 1
            result.append(x)

        counter_impact += 1

        if break_end: break
        counter_impact += 1

    return result
