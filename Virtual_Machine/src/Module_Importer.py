import importlib
import os

def get_modules():
    modules = []
    folder_list = os.listdir("Modules/.")
    for i in range(len(folder_list)):
        if folder_list[i].endswith(".py") and folder_list[i] != "__init__.py":
            folder_list[i] = remove_extension(folder_list[i])
            modules.append(importlib.import_module("Modules.{}".format(folder_list[i])))
    return modules




def remove_extension(folder_name):
    return folder_name.replace(".py", "")
