import sys


def run():
    o = open(sys.argv[2], 'w')

    o.write("/*------------------------\\\n"
            "|  Created With FileTC    | \n"
            "\\------------------------*/\n\n")


    o.write(f"const char* {sys.argv[3]} =\n")

    with open(sys.argv[1], "r") as i:
        for line in i:
            o.write("\"" + f"{line[:-1]}" + "\\n\"\n")

    o.write("\"\\0;\"")


run()
