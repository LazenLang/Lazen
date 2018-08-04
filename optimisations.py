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

        # print("x: ", x)
        if x == "+":
            get_before = token_list[counter - 1]
            if get_before in info.tokenizing_symbols:
                counter += 1
                continue
        """elif x == "-":
            # -5
            # -(5+5)
            # 5-5
            get_before = " "
            # for cnter, x9 in enumerate(token_list):
            #    print("x9: ", x9, " / ", cnter)

            if counter - 1 >= 0:
                get_before = token_list[counter - 1]
                if get_before in info.tokenizing_symbols and not get_before == ")":
                    if len(token_list) >= counter + 1:
                        get_after = token_list[counter + 1]
                        print("get_after: ", get_after)
                        if get_after == "(":
                            print("")
                        else:
                            result.append("(")
                            result.append("0")
                            result.append("-")
                            result.append(get_after)
                get_before = token_list[counter - 1]
                            result.append(")")
                            print("after it should be ", token_list[counter + 1], " and then ", token_list[counter + 2])
                            print("but now it's ", token_list[counter])
                            counter += 2
                            continue
            elif counter - 1 == -1:
                print("") """
        #get_before = " "
        get_after, get_after_db = " ", " "
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
        return result
