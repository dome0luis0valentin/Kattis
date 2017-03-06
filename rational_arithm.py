import sys

def reduce_frac(a,b):
    num1 = a
    num2 = b
    while a%b != 0:
        c = a
        a = b
        b = c % b

    return num1/b , num2/b

def add(a,b,c,d):
    return a*d + c*b, b*d
def mult(a,b,c,d):
    return a*c,b*d

def main():
    next(sys.stdin)
    for line in sys.stdin:
        n = line.strip().split()
        operation = n[2]
        if operation == "+":
            n1,n2 = add(int(n[0]),int(n[1]),int(n[3]),int(n[4]))
        elif operation == "-":
            n1,n2 = add(int(n[0]),int(n[1]),-1*int(n[3]),int(n[4]))
        elif operation == "*":
            n1,n2 = mult(int(n[0]),int(n[1]),int(n[3]),int(n[4]))
        else:
            n1,n2 = mult(int(n[0]),int(n[1]),int(n[4]),int(n[3]))

        n1,n2 = reduce_frac(n1,n2)
        print n1,"/",n2

main()
