import info
import traceback
import text_utilities
import tokenizer
def tokenizer_optimize(token_list_raw, first_time = False):
    # Basic Tokens Optimisations, Examples -
    # +1 -> 1 | +(1+1) -> (1+1)
    # -1 -> (0-1) | -(5+5) -> (0-(5+5))
    # 1++ -> (1+1) | (1+5)++ -> ((1+5)+1)

    token_list = []
    for x in token_list_raw:
        to_app = x
        if not x == " ": to_app = x.strip()
        else: to_app = x
        token_list.append(to_app)

    result_raw, counter_impact, break_end = [], 0, False

    for counter in range(0, len(token_list)):
        if counter_impact > len(token_list)-1: break
        get_after, x = "", token_list[counter_impact]

        try:
            get_after = token_list[counter_impact + 1]
        except:
            break_end = True

        allowed_funcs = ["for", "print", "if", "while", "elif", "return"]
        if first_time and not x in info.tokenizing_symbols and not get_after.strip() \
        in info.tokenizing_symbols and counter == 0 and x.strip() in allowed_funcs:
            result_raw.append(x)
            result_raw.append("$")
            result_raw.append("(")
            for x2 in token_list[counter_impact + 1 : len(token_list)]:
                result_raw.append(x2)
            result_raw.append(")")
            break

        if x == "!" and get_after == "=": result_raw.append("!=")

        elif x == "=" and get_after == "=": result_raw.append("==")
        elif x == "<" and get_after == "=": result_raw.append("<=")
        elif x == ">" and get_after == "=": result_raw.append(">=")
        elif x == "+" and get_after == "=": result_raw.append("+=")
        elif x == "-" and get_after == "=": result_raw.append("-=")
        elif x == "/" and get_after == "=": result_raw.append("/=")
        elif x == "*" and get_after == "=": result_raw.append("*=")
        elif x == "^" and get_after == "=": result_raw.append("^=")
        elif x == "%" and get_after == "=": result_raw.append("%=")
        elif x == "&" and get_after == "=": result_raw.append("&=")
        elif x == "&" and get_after == "&": result_raw.append("&&")
        elif x == "§" and get_after == "§": result_raw.append("§§")
        elif x == ":" and get_after == "¨": result_raw.append(":¨")
        elif x == "|" and get_after == "|": result_raw.append("||")

        elif x.lower() == "and":
            counter_impact -= 1
            result_raw.append("&&")
        elif x.lower() == "in":
            counter_impact -= 1
            result_raw.append("§§")
        elif x.lower() == "or":
            counter_impact -= 1
            result_raw.append("||")
        elif x.lower() == "is":
            counter_impact -= 1
            result_raw.append("==")
        elif x.lower() == "not":
            counter_impact -= 1
            result_raw.append(":¨")
        elif x.lower() == "isnt":
            counter_impact -= 1
            result_raw.append("!=")

        elif not x in info.tokenizing_symbols and not x == "@" and not x == "$" and get_after == "(":
            counter_impact -= 1
            result_raw.append(x)
            result_raw.append("@")
        else:
            counter_impact -= 1
            result_raw.append(x)

        counter_impact += 1

        if break_end: break
        counter_impact += 1

    result = []
    for x in result_raw:
       result.append(x.replace("\t", ""))
    return result
