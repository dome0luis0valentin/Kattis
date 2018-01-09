import sys
cross_section = []
change_list = [(-1,0),(0,-1),(0,1),(1,0)]
n,m = 0,0
def mark_rings():
    global cross_section
    curr_ring = 0
    done = False
    while(not done):
        done = True
        for y in xrange(n):
            for x in xrange(m):
                if cross_section[y][x] == curr_ring:
                    for dy,dx in change_list:
                        x_p,y_p = (x+dx),(y+dy)
                        if  (0 <= x_p < m)  and  (0 <= y_p < n):
                            if (cross_section[y_p][x_p]==-1):
                                cross_section[y_p][x_p] = curr_ring+1
                                done = False
        curr_ring += 1
    return curr_ring


def pretty_print(max_ring):
    space = 2 if max_ring<10 else 3
    for row in cross_section[1:-1]:
        new_row = []
        for val in row[1:-1]:
            if val == 0:
                new_row.append("."*space)
            else:
                new_row.append(str(val).rjust(space,"."))
        print "".join(new_row)


def main():
    global cross_section,n,m
    n,m = [int(i) for i in sys.stdin.readline().split()]
    cross_section.append([0 for i in xrange(m+2)])
    for line in sys.stdin:
        line = line.strip()
        row = [0]
        for c in line:
            if c == '.':
                row.append(0)
            else:
                row.append(-1)
        row.append(0)
        cross_section.append(row)

    cross_section.append([0 for i in xrange(m+2)])
    n,m = n+2,m+2
    pretty_print(mark_rings())

if __name__ == '__main__':
    main()
