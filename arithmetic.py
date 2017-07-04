import sys

def main():
    f = open(sys.argv[1],"r")
    var = {}
    for line in f:
        line = line.split()
        sign = 1
        result = 0
        equ = []
        ops = []
        # if line is a variable defination
        if len(line) == 3 and line[1] == "=":
            var[line[0]] = int(line[-1])
        # if line is a calculation
        else:
            for token in line:
                num = 0
                try:
                    num = int(token)
                    result += sign*num
                except ValueError:
                    if token in var:
                        result += sign*var[token]
                    elif token == "+":
                        sign = 1
                    elif token == "-":
                        sign = -1
                    else:
                        equ.append(token)
                        ops.append(sign)

            # now printing
            if result == 0:
                output = ""
            else:
                output = str(result)

            for s,x in zip(ops,equ):
                if s == 1:
                    if len(output) == 0:
                        output += x
                    else:
                        output += " + " + x
                elif s == -1:
                    output += " - " + x


            print output


if __name__ == '__main__':
    main()
