<<<<<<< HEAD
import sys
import math

def main():

    D = int(sys.stdin.readline().strip()) # distance
    sqrt_D = int(math.sqrt(D))
    if sqrt_D**2 == D:
        print 0, sqrt_D
        return
    for i in range(int(math.sqrt(D)),0,-1):
        if (D % i == 0):
            n2 = D/i # second factor
            b = int((n2 - i)/2.0) # possible b
            a_2 = D + b*b # possible a^2
            a = int(math.sqrt(a_2))
            if (a*a == a_2 ) and (a**2 - b**2):
                print b,a
                return
    print "impossible"

if __name__ == '__main__':
    main()
=======
import sys
import math

def main():

    D = int(sys.stdin.readline().strip()) # distance
    sqrt_D = int(math.sqrt(D))
    if sqrt_D**2 == D:
        print 0, sqrt_D
        return
    for i in range(int(math.sqrt(D)),0,-1):
        if (D % i == 0):
            n2 = D/i # second factor
            b = int((n2 - i)/2.0) # possible b
            a_2 = D + b*b # possible a^2
            a = int(math.sqrt(a_2))
            if (a*a == a_2 ) and (a**2 - b**2):
                print b,a
                return
    print "impossible"

if __name__ == '__main__':
    main()
>>>>>>> f177bf73e7319f758524fdec06543bad31a6230d
