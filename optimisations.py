import info
import traceback
import text_utilities
import tokenizer
def tokenizer_optimize(token_list, phase = 1):
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

        assemble = str(x) + str(get_after)

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

        else:
            counter_impact -= 1
            result.append(x)

        counter_impact += 1

        if break_end: break
        counter_impact += 1

    return result
