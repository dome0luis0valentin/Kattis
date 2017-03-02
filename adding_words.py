import sys

def main():
    var = {}
    values = {}
    #f = open(sys.argv[1],"r")
    for line in sys.stdin:
        line  = line.split()
        command = line[0]
        if command.lower() == "def":
            x,y = line[1:]
            var[x] = int(y)
            values[int(y)] = x
        elif command.lower() == "calc":
            sign = 1
            ans = 0
            for i in line[1:]:
                if i in var:
                    ans += sign*var[i]
                elif i == "+":
                    sign = 1
                elif i == "-":
                    sign = -1
                elif i == "=":
                    if ans in values:
                        ans = values[ans]
                    else:
                        ans = "unknown"
                    break
                else:
                    ans = "unknown"
                    break
            print " ".join(line[1:]),ans
        else:
            var.clear()
            values.clear()

if __name__ == '__main__':
    main()
