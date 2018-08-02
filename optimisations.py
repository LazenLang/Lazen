import info
import traceback
import text_utilities
import tokenizer
def tokenizer_optimize(token_list, phase = 1):
    # Basic Tokens Optimisations, Examples -
    # +1 -> 1 | +(1+1) -> (1+1)
    # -1 -> (0-1) | -(5+5) -> (0-(5+5))
    # 1++ -> (1+1) | (1+5)++ -> ((1+5)+1)
    result = []
    counter = 0
    for i in token_list:
        x = ""
        try:
            x = token_list[counter]
        except:
            break
        #get_before = " "
        get_after = " "
        get_after_db = " "
        try:
            #get_before = token_list[counter - 1]
            get_after = token_list[counter + 1]
            get_after_db = token_list[counter + 2]
        except:
            pass

        # 40:+:(:5:+:+:)
        if (get_after == "+" and get_after_db == "+" and (not x in info.tokenizing_symbols or x == ")")) or \
        (get_after == "-" and get_after_db == "-" and (not x in info.tokenizing_symbols or x == ")")):
            if x == ")":
                get_btwn_parn, opening_parn = "", 0 # get_btwn_parn is including parenthesis themselves

                for i2 in reversed(range(0, counter + 1)):
                    x2 = token_list[i2]
                    get_btwn_parn += x2
                    if x2 == ")":
                        opening_parn += 1
                    elif x2 == "(":
                        opening_parn -= 1

                    if opening_parn == 0:
                        break

                get_btwn_parn = text_utilities.reverse_str(get_btwn_parn)
                result = result[0 : counter - (len(get_btwn_parn)-1)]

                result.append("(")
                result.append(get_btwn_parn)
                result.append(get_after)
                result.append("1")
                result.append(")")

                counter += 2
            else:
                result.append("(")
                result.append(x)
                result.append(get_after)
                result.append("1")
                result.append(")")
                counter += 2
        else:
            result.append(x)
        counter += 1
    if phase <= 2:
        return tokenizer_optimize(result, phase + 1)
    else:
        print("res len: ", len(result))
        return result
