import sys

def main():
    #f = open(sys.argv[1],"r")
    variables = {}
    for line in sys.stdin:
        line = line.split()
        if line[0] == "define":
            variables[line[-1]] = line[1]
        else:
            if line[1] in variables and line[-1] in variables:
                if line[2] != "=":
                    if eval(variables[line[1]] + line[2] + variables[line[-1]]):
                        print "true"
                    else:
                        print "false"
                else:
                    if eval(variables[line[1]] + "==" + variables[line[-1]]):
                        print "true"
                    else:
                        print "false"
            else:
                print "undefined"

if __name__ == '__main__':
    main()
