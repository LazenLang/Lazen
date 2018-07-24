import info
def tokenizer_optimize(token_list):
            # Basic Tokens Optimisations, Example : print(5--5) -> print(5-(0-5)) -> print(5+5)
            # or print(5++5) -> print(5+5)
            # or print(5 + -5) -> print(5 + (0-5))
            # or print(5-- + 8) -> print((5-1) + 8) or print(5++ + 8) -> print((5+1) + 8)
    print("")
