import sys

def main():
    n = sys.stdin.readline().strip()
    m = len(sys.stdin.readline().strip())-1

    if len(n) > m:
        index = len(n)-m
        rest = n[index:].strip("0")
        if len(rest)>0:
            print n[:index]+"."+rest
        else:
            print n[:index]
    else:
        print "0."+("0")*(m-len(n))+n

if __name__ == '__main__':
    main()
