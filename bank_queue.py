import sys

class Container:
    def __init__(self,val,index):
        self.i = index
        self.val = val
    def __gt__(self,other):
        return self.val > other.val

    def __repr__(self):
        return str((self.val,self.i))


def main():
    #sys.stdin = open(sys.argv[1],"r")
    n,m = [int(i) for i in sys.stdin.readline().split()]
    choices = dict([(i,[]) for i in range(m+1)])

    coin_dict = {}
    for i in range(n):
        coin,time = [int(j) for j in sys.stdin.readline().split()]
        coin_dict[i] = coin
        for j in range(min(time,m)+1):
            choices[j].append(i)


    ans = 0
    forbidden = set([])
    for t in range(m,-1,-1):
        seq = choices[t]
        val = []
        for k in seq:
            if k not in forbidden:
                val.append(Container(coin_dict[k],k))

        if len(val) != 0:
            x = max(val)
            forbidden.add(x.i)
            ans += x.val
    print ans

if __name__ == '__main__':
    main()
