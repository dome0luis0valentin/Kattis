import sys

def all_from(board, m, n, k, start):
    winner = None
    #c, f
    x,y = start
    ch = board[x][y]
    count = 0

    #Recorrer horizontal hasta completar fila de k
    if y+k <= n:
        ch = board[x][y]
        count = 1

        for y in range(y+1, n):
            if board[x][y] != ch:
                break
            else:
                count += 1

        if count == k:
            winner = ch
            return winner
    
    x,y = start
    #Recorrer vertical hasta completar columna de k
    if x+k <= m :
        ch = board[x][y]
        count = 1

        for x in range(x+1, m):
            if board[x][y]!= ch:
                break
            else:
                count +=1

        if count == k:
            winner = ch
            return winner
    
    x,y = start
    #Recorrer diagonal a derecha hacia abajo hasta completar diagonal de k
    if x+k <= m  and y+k <= n:
        ch = board[x][y]
        count = 1
        
        for i in range(1, k):
            if board[x+i][y+i] != ch:
                break
            else:
                count += 1

        if count == k:
            winner = ch
            return winner
    
    x,y = start
    #Recorrer diagonal a izquierda hacia abajo hasta completar diagonal de k
    if x+k <= m and y-k+1 >= 0:
        ch = board[x][y]
        count = 1
        
        for i in range(1, k):
            if board[x+i][y-i] != ch:
                break
            else:
                count += 1

        if count == k:
            winner = ch
            return winner
    
    return winner

def solve(board, m, n,  k):
    #M Filas
    #N columnas
    winner = None
    for f in range(m):
        for c in range(n):
            #Busca de arriba a abajo, o de izquierda a derecha, en linea recta o en diagonal
            #No vulve a abajo, porque si existe la linea la tendría que haber encontrado
            if board[f][c] != ".":
                winner = all_from(board,m, n,k, (f, c))
            if winner:
                break
        if winner:
            break

    if winner:
        if winner == "x":
            return 1,0
        else:
            return 0,1
    else:
        return 0,0

# def main():
#     #Función que lee una línea de la entrada
#     line = lambda : sys.stdin.readline().strip()

#     #Cantidad de casos a leer
#     cases = int(line())

#     #Tamaño de la grilla y de la palabra
#     m, n, k = map(int, line().split())
#     score = [0, 0]

#     #Para cada caso
#     for c in range(cases):
#         board = [line() for i in range(n)]

#         won_gretel = solve(board,m, n, k)
#         if won_gretel != None:
#             if won_gretel:
#                 score[0] = score[0] + 1
#             else:
#                 score[1] = score[1] + 1

#     print(f"{score[0]}:{score[1]}")

def main():
    hansel, gretel = 0, 0
    cases = int(input().strip())

    for case in range(cases):
        board = []
        n, m, k = [int(i) for i in input().split()]
        for row in range(m):
            line = input().strip()
            board.append(list(line))
        h, g = solve(board,m, n, k)
        hansel += h
        gretel += g
    print(str(hansel) + ":" + str(gretel))

if __name__ == '__main__':
    main()

#Contribución de Domé Valentin
