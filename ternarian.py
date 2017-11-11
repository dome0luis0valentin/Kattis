import sys,math,bisect

pow_of_3 = [1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441,
            1594323, 4782969, 14348907, 43046721, 129140163, 387420489, 1162261467]

def base_3(n):
    base3 = []
    if n == 0:
        print "left pan:"
        print "right pan:"
        return
    bits  = int(math.log(n,3)) + 1
    val = 3**(bits+1)
    for i in xrange(bits,-1,-1):
        val /= 3
        if 2*val <= n:
            base3.append(2)
            n -= 2*val
        elif val <= n:
            base3.append(1)
            n -= val
        else:
            base3.append(0)

    balanced = balance_tri(base3)
    left,right = ["left pan:"], ["right pan:"]
    bal_len = len(balanced)
    val = 3**bal_len
    for i in xrange(bal_len):
        val /= 3
        if balanced[i] == -1:
            left.append(str(val))
        elif balanced[i] == 1:
            right.append(str(val))
    print " ".join(left)
    print " ".join(right)



def balance_tri(base3):
    balanced = []
    carry = 0
    for i in reversed(base3):
        if i+carry<=1:
            balanced.append(i+carry)
            carry = 0
        elif i+carry == 2:
            carry = 1
            balanced.append(-1)
        elif i+carry == 3:
            balanced.append(0)
            carry = 1
    return balanced[::-1]

def main():
    n = int(sys.stdin.readline().strip())
    for line in range(n):
        base_3(int(sys.stdin.readline().strip()))
        print

if __name__ == '__main__':
    main()
