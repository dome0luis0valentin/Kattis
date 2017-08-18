import sys,math

def main():
    n = sys.stdin.readline().strip()
    length = len(n)
    facts_set = {'1':1, '2':2, '6':3, '24':4, '120':5, '720':6}
    if n in facts_set:
        print facts_set[n]
        return

    fact_len = 0.0
    i = 0
    while int(fact_len)+1 != length:
        i += 1
        fact_len += math.log(i,10)
    print i

if __name__ == '__main__':
    main()
