import sys
def sub_seq(seq,d):
    prefix = [0]
    c = 1
    for i in seq:
        prefix.append(prefix[-1]+i)
        c +=1

    total = 0
    for j in range(c-1):
        for k in range(j+1,c):
            if (prefix[k]-prefix[j])%d == 0:
                total += 1
    return total
def main():
    #sys.stdin = open(sys.argv[1],"r")
    cases = int(sys.stdin.readline().strip())
    for c in range(cases):
        d,n = [int(k) for k in sys.stdin.readline().split()]
        line = sys.stdin.readline().split()
        val = 0
        count = [0 for i in range(d)]
        for i in range(len(line)):
            val = (int(line[i]) + val)%d
            count[val] += 1
        total = 0
        for i in count:
            total += (i*(i-1))/2


        print total+count[0]

if __name__ == '__main__':
    main()
