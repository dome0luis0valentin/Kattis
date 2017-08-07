import sys

def parent(n,connection_map):
    n = connection_map[n]
    visited = []
    while n!=connection_map[n]:
        n = connection_map[n]
        visited.append(n)

    for i in visited:
        connection_map[i]=n

    return n


def main():
    max_r, max_c = [int(i) for i in sys.stdin.readline().split()]
    connection_map = [i for i in xrange(max_r*max_c)]

    complete_map = []
    for r in range(max_r):
        row = []
        line = sys.stdin.readline().strip()
        for c in range(max_c):
            curr_val = int(line[c])
            row.append(curr_val)
            curr_id = r*max_c + c
            p1,p2 = curr_id,curr_id
            b1,b2 = False,False
            if r>0: # can safely check up
                if curr_val == complete_map[r-1][c]:
                    p1 = parent((r-1)*max_c+c,connection_map)
                    b1 = True
            if c>0: # can safely check left
                if curr_val == row[c-1]:
                    p2 = parent((r*max_c)+c-1,connection_map)
                    b2 = True

            real_parent = min(p1,p2)
            connection_map[r*max_c + c ] = real_parent

            if b1 and b2:
                if p1 > p2:
                    connection_map[p1] = p2
                else:
                    connection_map[p2] = p1

        complete_map.append(row)
    # Now handle queries
    queries = int(sys.stdin.readline().strip())
    for q in range(queries):
        r1,c1,r2,c2 = [int(i)-1 for i in sys.stdin.readline().split()]
        if complete_map[r1][c1] != complete_map[r2][c2]:
            print 'neither'
        elif parent(r1*max_c+c1,connection_map) == parent(r2*max_c+c2,connection_map):
            if complete_map[r1][c1]:
                print 'decimal'
            else:
                print 'binary'
        else:
            print 'neither'

if __name__ == '__main__':
    main()
