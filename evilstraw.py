import sys

def make_pali(a_str):
    x = len(a_str)
    if x <=1:
        return 0,True
    if x == 2:
        return 0,a_str[0]==a_str[1]

    count  = 0
    for k in range(len(a_str)):
        letter = a_str[0]
        for i in range(x-1,0,-1):
            if letter == a_str[i]:
                a,b = make_pali(a_str[1:i]+a_str[i+1:])
                if b:
                    return (x - (i+1)) + a + count, True
                else:
                    return 0, False
        a_str = a_str[1]+a_str[0]+a_str[2:]
        count +=1
    return 0,False

def main():
    #f = open(sys.argv[1],"r")
    next(sys.stdin)
    for i in sys.stdin:
        a,b = make_pali(i.strip())
        if b:
            print(a)
        else:
            print ("Impossible")


if __name__ == '__main__':
    main()
