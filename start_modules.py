import tokenizer, optimisations, errors, text_utilities, ast_build, ast_analysis

def go(code):
    verify_closings = errors.unclosed_symbols_verification(code)
    if len(verify_closings) > 1:

        if verify_closings[1] == "char": errors.pup_error(errors.get_error("0004", [str(verify_closings[2] + 1)]))
        elif verify_closings[1] == "str": errors.pup_error(errors.get_error("0005", [str(verify_closings[2] + 1)]))
        elif verify_closings[1] == "tmop": errors.pup_error(errors.get_error("0006", [str(verify_closings[2] + 1)]))
        elif verify_closings[1] == "tmcp": errors.pup_error(errors.get_error("0007", [str(verify_closings[2] + 1)]))

    else:
        for counter, x in enumerate(tokenizer.go(code, True)):
            errors.bsc_syntx_errs(x, counter, True) # This will check for invalid characters in x
            # Token-list optimizer is temporarily unstable, it can cause errors.

            optimize_x = optimisations.tokenizer_optimize(x, True)
            errors.bsc_syntx_errs(optimize_x, counter) # This function will quit() and print the error
                                                        # it encountered if it encounters a minor syntaxic error.

            if not len(optimize_x) > 0:
                continue
            x2 = ast_build.go(optimize_x) # Here we're building an abstract syntax tree from the optimized token list.

            if ast_analysis.go(x2):
                print("we have to parse ", optimize_x)
                print(x2)
                print("-----------")
