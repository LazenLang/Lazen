import sys
import info
import errors
import start_modules
import text_utilities

file_to_interpret = ""

print("a" is "b" is "a")

for counter, x in enumerate(sys.argv):
    if x.startswith("--"):
        raw_arg = x[2 : len(x)]
        if raw_arg.lower() == "file":
            try:
                err_test = sys.argv[counter + 1]
            except:
                errors.pup_error(errors.get_error("0001"))

            file_name = " "
            for x2 in range(counter + 1, len(sys.argv)):
                if not sys.argv[x2].startswith("--"):
                    file_name += sys.argv[x2] + " "
                else:
                    break

            file_name, file_read = file_name.strip(), ""

            try:
                fstream = open(file_name)
                file_read = fstream.read()
                fstream.close()
            except:
                errors.pup_error(errors.get_error("0002", file_name))

            start_modules.go(file_read)



        elif raw_arg.lower() == "help":
            print(info.help)
            quit()
        elif raw_arg.lower() == "version":
            print("Lazen Interpreter (" + info.version + ")")
            quit()
