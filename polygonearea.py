import sys
import math

def area(points):
    total = 0
    pivot = points[0]
    i=0
    l = len(points)
    while i < l:
        total += (int(points[(i+1)%l][0]) *
                  (int(points[(i+2)%l][1]) - int(points[(i)%l][1])))
        i+=1
    if total > 0:
        lable = "CCW"
    else:
        lable = "CW"
    return lable, 0.5*abs(total)

def main():
    poly_point = []
    for line in sys.stdin:
        if line.strip().isdigit():
            if len(poly_point) != 0:
                lable,area_val = area(poly_point)
                print lable,area_val
                poly_point = []
        else:
            poly_point.append(line.strip().split())

if __name__ == "__main__":
    main()
