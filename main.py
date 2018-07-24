import sys
import info
import errors
import start_modules

counter = 0
file_to_interpret = ""

for i in sys.argv:
    if i.startswith("--"):
        raw_arg = i[2 : len(i)]
        if raw_arg.lower() == "file":
            try:
                err_test = sys.argv[counter + 1]
            except:
                errors.pup_error(errors.get_error("0001"))

            file_name = " "
            for i2 in range(counter + 1, len(sys.argv)):
                if not sys.argv[i2].startswith("--"):
                    file_name += sys.argv[i2] + " "
                else:
                    break

            file_name = file_name.strip()

            file_read = ""
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
    counter += 1
