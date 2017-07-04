import sys

def pow_mod(a,b,n):

    a = int(a)
    b = int(b)
    n = int(n)

    b = bin(b)[2:]
    pow_list = []
    num = a
    for i in reversed(b):
        if int(i) == 1:
            pow_list.append(num)
        num = (num**2) % n

    total = 1
    for term in pow_list:
        total = (term*total) % n
    return (total*8)%n

def main():
    f = open(sys.argv[1],"r")
    n = f.readline()
    for line in f:
        d = int(line.strip())
        res = power_mod(9,d-1,1000000007)
        print d
        print res

if __name__ == '__main__':
    main()
