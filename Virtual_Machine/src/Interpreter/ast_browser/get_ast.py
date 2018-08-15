
#Permet d'avoir la ligne d'arrêt de l'AST et d'avoir cette partie de l'AST pour pouvoir l'utiliser plus tard
def get_ast(code, starting_line):
    ast_line = 0
    in_ast = True
    ast_code = []
    while in_ast == True:
        if code[ast_line + starting_line].replace("\n", "") == "}":
            break
        ast_code.append(code[starting_line+ast_line])
        ast_line += 1
    return ast_line, ast_code[0]
#Outil de développement pour afficher un ast
def print_ast(ast):
    for x in range(line_number):
        print(ast[x])
