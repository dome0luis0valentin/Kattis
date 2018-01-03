import sys

def main():
    sys.stdin.readline()
    for line in sys.stdin:
        k,r = line.split()
        p,q = [int(i) for i in r.split("/")]
        if p==q:
            p,q = 1,2
        elif p<q:
            p,q = q,q-p
        elif q==1: # special case of below, no need for calculation 
            p,q = q,p+1
        else:
            count = int(p/q)
            p,q = p%q,q # find common sibling (sibling from commmon ancestor)
            p,q = q,q-p # find sibling, ancestor of next
            p,q = p,q+p*count # find next

        print k,"{0}/{1}".format(p,q)

if __name__ == '__main__':
    main()
