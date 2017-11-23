import sys
# test case to test => 5 1 6 6 6 => should give 4

def min_possible_vl(min_maxes,prefix,l,count):
    max_v = prefix[-1]
    for i in xrange(l-2,-1,-1):
        val = max_v - prefix[i]
        if val >= min_maxes[i]:
            min_maxes.append(val)
            count.append(count[i]+1)
            return True
    return False

def main():
    sys.stdin.readline()
    line = sys.stdin.readline().split()

    count = [0]
    prefix = [0]
    min_maxes = [0]
    l = 1
    for i in line:
        num = int(i)
        prefix.append(prefix[-1]+num)
        l += 1
        min_possible_vl(min_maxes,prefix,l,count)

    print count[-1]

if __name__ == '__main__':
    main()
