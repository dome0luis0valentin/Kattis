import sys

def main():
    n,s,k = [int(i) for i in sys.stdin.readline().split()]
    prev = [0]*(k+1)
    prev [0] = 1
    now = [1]*(k+1)

    for i in xrange(1,n+1):
        for j in xrange(1,k+1):
            # ==> prev[j] is prob of getting j with i-1 tries (multiply with
            #     probability of not getting a new number on this roll)
            #     So one of j-1 already found rolls
            # ==> prev[j-1] is prob of getting j-1 with i-1 trie (multiply with
            #     probability of getting a new number on this roll)
            
            # PROBABLITY OF NOT FINIDING A NEW ROLL
            p = (j-1)/(s*1.0)
            now[j] = prev[j]*p + prev[j-1]*(1-p)
        prev = now
        now = [1]*(k+1)
    print prev[k]


if __name__ == '__main__':
    main()
