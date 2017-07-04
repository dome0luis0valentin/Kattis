import sys
def difference_engine(seq):
    if len(seq)==1:
        return 0,seq[0]
    flag = False
    new = [seq[0]-seq[1]]
    for i in range(1,len(seq)-1):
        new.append(seq[i]-seq[i+1])
        if new[-1]!=new[-2]:
            flag = True


    if flag:
        power,last = difference_engine(new)
        return power+1,seq[-1]-last
    else:
        return 1,seq[-1]-new[-1]


def main():
    seq = [int(i) for i in sys.stdin.readline().split()[1:]]
    p,n = difference_engine(seq)
    print p,n

if __name__ == '__main__':
    main()
