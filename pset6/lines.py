import sys



if len(sys.argv) == 2 and sys.argv[-1].endswith(".py"):
    try:
        with open(sys.argv[-1], "r") as file:
            line_counter = 0
            for line in file:
                 if not line.lstrip().startswith("#") and line.lstrip() != "":
                     line_counter += 1
        print(line_counter)
    except FileNotFoundError:
        sys.exit("File does not exist")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) == 2 and not sys.argv[-1].endswith(".py") :
        sys.exit("Not a Python file")
