import sys,math

FACTS = [0.0,0.0]
def fact_digits(n):
    length = len(FACTS)
    if n < length:
        return FACTS[n]
    for i in range(length,n+1):
        FACTS.append(FACTS[i-1] + math.log(i,10))
    return FACTS[n]

def main():
    for i in sys.stdin:
        if int(i.strip()) <= 1:
            print 1
        else:
            print int(math.ceil(fact_digits(int(i.strip()))))

if __name__ == '__main__':
    main()
