#Function that print a label
class LazenFunction:
    def __init__(self):
        self.funcname = "out"
    def func_code(self, line):
        line = line.split(":")
        print(line[1])
