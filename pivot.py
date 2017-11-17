import sys

def main():
    n = int(sys.stdin.readline().strip())
    a_t = [int(i) for i in sys.stdin.readline().split()]
    min_v, max_v = [a_t[-1]],[a_t[0]]
    for i in range(1,n):
        j = n-1-i
        # from back
        min_v.append(min(a_t[j],min_v[-1]))
        # from front
        max_v.append(max(a_t[i],max_v[-1]))
    count = 0
    for i in range(n):
        j = n-1-i
        if max_v[i] <= a_t[i] and a_t[i] <= min_v[j]:
            count += 1
    print count


if __name__ == '__main__':
    main()
