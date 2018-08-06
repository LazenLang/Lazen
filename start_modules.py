import tokenizer
import optimisations
import errors
import parsing
import text_utilities

def go(code):
    verify_closings = errors.unclosed_symbols_verification(code)
    if len(verify_closings) > 1:
        if verify_closings[1] == "char":
            errors.pup_error(errors.get_error("0004", str(verify_closings[2] + 1)))
        elif verify_closings[1] == "str":
            errors.pup_error(errors.get_error("0005", str(verify_closings[2] + 1)))
        elif verify_closings[1] == "tmop":
            errors.pup_error(errors.get_error("0006", str(verify_closings[2] + 1)))
        elif verify_closings[1] == "tmcp":
            errors.pup_error(errors.get_error("0007", str(verify_closings[2] + 1)))
    else:
        for i in tokenizer.go(code, True):
            # Token-list optimizer is temporarily unstable, it can cause errors.
            optimize_i = optimisations.tokenizer_optimize(i, True)

            if not len(optimize_i) > 0:
                continue
            i2 = parsing.go(optimize_i)

            print("we have to parse ", optimize_i)
            print(i2)
            print("-----------")
