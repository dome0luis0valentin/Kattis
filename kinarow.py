import sys

def winner(b,n,m,k):
    for r in range(m):
        for c in range(n):
            side = b[r][c]
            if  side == "o" or side == "x":
                right,down,right_d,right_u = False,False,False,False
                # check down
                if r+k-1 < m:
                    down = True
                    for i in range(1,k):
                        if b[r+i][c]!=side:
                            down = False
                            break
                # check right
                if c+k-1 < n:
                    right = True
                    for i in range(1,k):
                        if b[r][c+i]!=side:
                            right = False
                            break
                # check down-right diagonal
                if r+k-1 < m and c+k-1 < n:
                    right_d = True
                    for i in range(1,k):
                        if b[r+i][c+i]!=side:
                            right_d = False
                            break

                # check up-right diagonal
                if r-k-1 >= 0 and c+k-1 < n:
                    right_u = True
                    for i in range(1,k):
                        if b[r-i][c+i]!=side:
                            right_u = False
                            break

                if right or down or right_d or right_u:
                    #print r,c,side
                    if side == "o":
                        return 0,1
                    else:
                        return 1,0
    return 0,0

def main():
    hansel,gretel = 0,0
    cases = int(sys.stdin.readline().strip())

    for case in range(cases):
        board = []
        n,m,k = [int(i) for i in sys.stdin.readline().split()]
        for row in range(m):
            line = sys.stdin.readline().strip()
            board.append(list(line))
        h,g = winner(board,n,m,k)
        hansel += h
        gretel += g
    print str(hansel) + ":" + str(gretel)

if __name__ == '__main__':
    main()
