import tokenizer
import optimisations
import errors
def go(code):
    verify_closings = errors.unclosed_symbols_verification(code)
    if len(verify_closings) > 1:
        if verify_closings[1] == "char":
            errors.pup_error(errors.get_error("0004", str(verify_closings[2] + 1)))
        elif verify_closings[1] == "str":
            errors.pup_error(errors.get_error("0005", str(verify_closings[2] + 1)))
        elif verify_closings[1] == "too_much_opening_parn":
            errors.pup_error(errors.get_error("0006", str(verify_closings[2] + 1)))
        elif verify_closings[1] == "too_much_closing_parn":
            errors.pup_error(errors.get_error("0007", str(verify_closings[2] + 1)))
    else:
        for i in tokenizer.go(code):
            for i2 in i:
                print(i2)
            print("-----------")
