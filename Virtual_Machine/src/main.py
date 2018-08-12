#Test of the functions

import Module_Importer as Module_Manager
import Interpreter.Interpreter_Main as Interpreter
import time
modules = Module_Manager.get_modules()
modules_funcs = []
for i in range(len(modules)):
    modules_funcs.append(modules[i].LazenFunction())
print(modules_funcs)

I = Interpreter.Interpreter(['out:Hello World !'], modules_funcs)
