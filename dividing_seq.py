import sys,math

def main():
    n = int(sys.stdin.readline().strip())
    size = int(math.log(n,2))+1
    print size
    k = 1
    while k<=n:
        print k,
        k *=2
if __name__ == '__main__':
    main()
