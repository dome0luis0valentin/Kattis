import sys
from math import sin,cos,radians,sqrt

def main():
    cases = int(sys.stdin.readline().strip())
    for i in xrange(cases):
        commands = int(sys.stdin.readline().strip())
        x,y = 0.0,0.0
        angle = 90.0 # assuming that turtle starts facing up
        for j in xrange(commands):
            cmd,num = sys.stdin.readline().split()
            num = int(num)
            if cmd == 'lt':
                angle += num
            elif cmd == 'rt':
                angle -= num
            elif cmd == 'fd':
                y += sin(radians(angle))*num
                x += cos(radians(angle))*num
            elif cmd == 'bk':
                y -= sin(radians(angle))*num
                x -= cos(radians(angle))*num
        print int(round(sqrt(x*x + y*y)))

if __name__ == '__main__':
    main()
