import sys

def main():
    while (True):
        clues = int(sys.stdin.readline().strip())
        if clues == 0:
            return
        info = []
        upper_bound = -1
        lower_bound = 0
        divisors = []
        # collecting clues
        for i in range(clues):
            hint = sys.stdin.readline().strip()
            val = int(hint.split()[-1])
            if "less than" in hint:
                if upper_bound == -1 or upper_bound > val:
                    upper_bound = val
            elif "greater than" in hint:
                if lower_bound == -1 or lower_bound < val:
                    lower_bound = val
            else:
                divisors.append(val)

        # processing clues
        lower_bound +=1
        if upper_bound == -1:
            print "infinite"
        else:
            # now filtering
            poss_vals = [0 for i in range(upper_bound-lower_bound)]
            for d in divisors:
                start = (d-lower_bound)%d
                for k in xrange(start,upper_bound-lower_bound,d):
                    poss_vals[k]+=1
            # now printing outcome
            count = 0
            for i in xrange(upper_bound-lower_bound):
                if poss_vals[i] == len(divisors):
                    print i+lower_bound,
                    count += 1
            if count == 0:
                print "none",
            print

if __name__ == '__main__':
    main()
