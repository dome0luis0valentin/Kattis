<<<<<<< HEAD
import sys
import math

def choose(a,b):
    # a!/(b!(a-b)!)
    return math.factorial(a)/(math.factorial(b)*math.factorial(a-b))

def main():

    steps = int(sys.stdin.readline())

    for i in range(steps):
        line = sys.stdin.readline()
        line = line.split()
        R = int(line[0])
        S = int(line[1])
        X = int(line[2])
        Y = int(line[3])
        W = int(line[4])

        p = float(S - R + 1)/S # probalibty of binomial success
        total_p = 0.0

        for i in range(X,Y+1):
            curr_p = choose(Y,i)*math.pow(p,i)*math.pow((1-p),(Y-i))
            total_p += curr_p
        if (total_p*W > 1):
            print "yes"
        else:
            print "no"

if __name__ == '__main__':
    main()
=======
import sys
import math

def choose(a,b):
    # a!/(b!(a-b)!)
    return math.factorial(a)/(math.factorial(b)*math.factorial(a-b))

def main():

    steps = int(sys.stdin.readline())

    for i in range(steps):
        line = sys.stdin.readline()
        line = line.split()
        R = int(line[0])
        S = int(line[1])
        X = int(line[2])
        Y = int(line[3])
        W = int(line[4])

        p = float(S - R + 1)/S # probalibty of binomial success
        total_p = 0.0

        for i in range(X,Y+1):
            curr_p = choose(Y,i)*math.pow(p,i)*math.pow((1-p),(Y-i))
            total_p += curr_p
        if (total_p*W > 1):
            print "yes"
        else:
            print "no"

if __name__ == '__main__':
    main()
>>>>>>> f177bf73e7319f758524fdec06543bad31a6230d
