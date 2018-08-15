
def copy_module_to_code(code,module,functions):
    for i in range(len(functions)):
        code[functions[i]] = []
        for x in range(len(module[functions[i]])):
            code[functions[i]].append(module[functions[i]][x])
    return code

def get_code(file):
    code = {}
    current_func = None
    function = []
    for line in file:
        if line.startswith("@"):
            line = line.split("@")[1].split(":")[0]
            current_func = line
            code[current_func] = []
            function.append(line)
        elif line.startswith("#imprt"):
            line = line.split("#")[1].split(":")[1].replace("\n","")
            with open(line, "r") as f:
                functions, module = get_code(f)
                code = copy_module_to_code(code, module,functions)
        else:
            code[current_func].append(line)

    return function, code
