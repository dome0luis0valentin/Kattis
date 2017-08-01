import sys

def main():
    n = int(sys.stdin.readline().strip())
    vr = [False for i in range(n+1)]
    hr = [False for i in range(n+1)]
    vr_snipe = [False for i in range(2*n)]
    hr_snipe = [False for i in range(2*n)]

    for line in sys.stdin:
        x,y = [int(i) for i in line.split()]
        if vr[x] or hr[y] or vr_snipe[x-y] or hr_snipe[y+x]:
            print "INCORRECT"
            return
        else:
            vr[x] = True
            hr[y] = True
            vr_snipe[x-y] = True
            hr_snipe[y+x] = True
    print "CORRECT"

if __name__ == '__main__':
    main()
