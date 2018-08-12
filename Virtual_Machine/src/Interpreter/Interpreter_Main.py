class Interpreter:
    def __init__(self,file_content, modules):
        self.line = 0
        self.code = file_content
        self.funcs = modules
        self.execute_line(self.code[0])
    def execute_line(self,line):
        for i in range(len(self.funcs)):
            if line.startswith(self.funcs[i].funcname):
                self.funcs[i].func_code(line)
