import ast_browser.get_ast as bast
import code_loader.code_loader as code_loader
import utils.interpreter_utils as utils
import utils.interpreter_consts as const
import interpreter_funcs.funcs as funcs
import time
import sys
import datetime
class Interpreter:
    def __init__(self,file_content):
        self.line = {}
        self.file_content = file_content
        #self.funcs = modules
        self.var_list = {"int": {}, "lbl": {}, "flt": {}, "bool": {}}
        functions, code = code_loader.get_code(self.file_content)
        t0 = time.perf_counter()
        func = self.execute_func("main", code)
        if func == "0":
            t1 = time.perf_counter()
            final = t1-t0
            print("Code was successfully executed in %.20f" % final)
    def execute_line(self,line, code, func):
        line = line.replace("\n","")
        line = utils.get_arguments(line)
        if line[0] in const.var_names:
            if line[2] in const.fcall_names:
                self.var_list[line[0]][func][line[1]] = self.execute_func(line[3], code)
            else:
                ast_lines, ast_code = bast.get_ast(code[func], self.line[func]+1)
                #Temporary
                self.var_list[line[0]][func][line[1]] = ast_code
                self.line[func] = ast_lines + self.line[func]
        if line[0] in const.out_names:
            sys.stdout.write(self.var_list["lbl"][func][line[1]].replace('"',"") + "\n")
        if line[0] in const.return_names:
            return line[1]


        return None
    def execute_func(self, func, code):
        self.line[func] = 0
        self.var_list["int"][func] = {}
        self.var_list["lbl"][func] = {}
        self.var_list["flt"][func] = {}
        self.var_list["bool"][func] = {}
        for i in range(len(code[func])):
            line = self.execute_line(code[func][self.line[func]], code, func)
            if line != None:
                return line
            self.line[func] += 1

f = open("test.lzb", 'r')
i = Interpreter(f)
