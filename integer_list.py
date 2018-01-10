import sys

def execute(cmd,n):
    direction = 1
    start,end = 0,n
    for c in cmd:
        if c == "R":
            direction *=-1
        else:
            if direction == 1:
                start += 1
            else:
                end += -1
        if start > end:
            return 0,0,0
    return start,end,direction

def main():
    cases = int(sys.stdin.readline().strip())
    for i in xrange(cases):
        cmd = sys.stdin.readline().strip()
        n = int(sys.stdin.readline().strip())
        s,e,d = execute(cmd,n)
        if (d == 0):
            print "error"
            sys.stdin.readline()
        else:
            l = [i for i in sys.stdin.readline().strip()[1:-1].split(",")]
            print "["+",".join(l[s:e][::d])+"]"
if __name__ == '__main__':
    main()
