import info
import traceback
import text_utilities
import tokenizer
def tokenizer_optimize(token_list):
    # Basic Tokens Optimisations, Example : print(5 - -5) -> print(5-(0-5)) -> print(5+5)
    result = []
    for i in token_list:
        counter = 0
        line_result = []
        for i2_raw in range(0, len(i)):
            try:
                i2 = i[counter]
            except:
                break
            x = 0
            if i2 == "-":
                try:
                    if counter > 0:
                        get_before = i[counter - 1]
                        if get_before in info.tokenizing_symbols:
                            get_after = i[counter + 1]
                            if get_after == "(":
                                get_till_end = ["("]
                                opened_parenthesis_amount = 1
                                for i_counter in range(counter + 2, len(i)):
                                    i_text = i[i_counter]
                                    if i_text == "(":
                                        opened_parenthesis_amount += 1
                                    elif i_text == ")":
                                        opened_parenthesis_amount -= 1

                                    get_till_end.append(i_text)

                                    if opened_parenthesis_amount == 0:
                                        break
                                    # print("i_text: " + i_text)
                                line_result.append("(")
                                line_result.append("0")
                                line_result.append("-")
                                for _i in tokenizer_optimize(tokenizer.go(text_utilities.list_to_str(get_till_end))):
                                    for _i2 in _i:
                                        line_result.append(_i2)
                                line_result.append(")")
                                counter += len(get_till_end) + 1
                                continue
                                """
                                print(5 - -(5 * 2))

                                print
                                (
                                5
                                -
                                -
                                (
                                5
                                *
                                2
                                )
                                )


                                """
                            else:
                                line_result.append("(")
                                line_result.append("0")
                                line_result.append("-")
                                line_result.append(get_after)
                                line_result.append(")")
                                counter += 2
                                continue
                        else:
                            line_result.append(i2)
                    else:
                        line_result.append(i2)
                except Exception as e:
                    print(traceback.print_exc())
                    x += 1
            elif i2 == "+":
                try:
                    if counter > 0:
                        get_before = i[counter - 1]
                        if not get_before in info.tokenizing_symbols:
                            line_result.append(i2)
                    #    else:
                            # counter += 1
                            # continue
                        # print("hey : " + +5)
                except:
                    x += 1
            else:
                line_result.append(i2)
            counter += 1
        result.append(line_result)
        line_result = []
    return result
