import sys,time

def gcd(a,b):
    if a == b:
        return a
    if a == 0:
        return b
    if b == 0:
        return a
    if ~a & 1:
        if b&1:
            return gcd(a>>1,b)
        else:
            return gcd(a>>1,b>>1)<<1
    if ~b & 1:
        return gcd(a,b>>1)
    if (a>b):
        return gcd((a-b)>>1,b)
    return gcd((b-a)>>1,a)

def touch(c1,c2):
    x1,y1,r1 = c1
    x2,y2,r2 = c2
    return (x1 - x2)**2 + (y1 - y2)**2 == (r1+r2)**2

def main():
    f = open(sys.argv[1],"r")
    cases = int(f.readline().strip()) # number of cases
    for m in range(cases):
        rotation = []
        wheels = []
        n = int(f.readline().strip())
        for i in range(n):
            wheel = [int(k) for k in f.readline().strip().split()]
            if i==0:
                rotation.append((1,1,1)) # only first wheel rotates
            else:
                rotation.append((0,0,1))
            wheels.append(wheel)

        unknown = range(n)
        q = [0]
        while len(q)!=0:
            curr = q.pop()
            x1,y1,r1 = wheels[curr]
            rot1,p1,q1 = rotation[curr]
            for i in unknown:
                x2,y2,r2 = wheels[i]
                if rotation[i] == (0,0,1) and touch((x1,y1,r1),((x2,y2,r2))):
                    p2,q2 = r1*p1,r2*q1
                    d = gcd(p2,q2)
                    p2,q2 = p2/d, q2/d
                    rot2 = rot1*-1
                    rotation[i] = (rot2,p2,q2)
                    q.append(i)

        # now printing
        for o in range(n):
            velo = rotation[o]
            if velo[1]==0:
                print "not moving"

            elif velo[0] == 1:
                if velo[-1] == 1:
                    print velo[1],"clockwise"
                else:
                    print str(velo[1])+"/"+str(velo[-1]),"clockwise"
            elif velo[0] == -1:
                if velo[-1] == 1:
                    print velo[1],"counterclockwise"
                else:
                    print str(velo[1])+"/"+str(velo[-1]),"counterclockwise"


if __name__ == '__main__':
    main()
