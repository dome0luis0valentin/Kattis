<<<<<<< HEAD
import sys
WINS = [["paper","rock"],["rock","scissors"],["scissors","paper"]]

def main():
    line = sys.stdin.readline().split()
    while (True):

        n = int(line[0])
        k = int(line[1])

        total_games = int((k*n*(n-1))/2.0)
        play_info = [[0,0] for x in range(n)] # intialize player info list

        for i in range(total_games):
            game = sys.stdin.readline().split()
            p1 = int(game[0])
            p2 = int(game[2])
            m1 = (game[1])
            m2 = (game[3])

            if [m1,m2] in WINS:
                play_info[p1-1][0] +=1 # add wins to p1
                play_info[p2-1][1] +=1 # add loose to p2
            elif m1!=m2:
                play_info[p2-1][0] +=1 # add wins to p2
                play_info[p1-1][1] +=1 # add loose to p1

        for i in play_info:
            if i[1]+i[0] == 0:
                print "-"
            else:
                print "%.3f"% round((i[0]*1.0)/(i[0]+i[1]),3)

        line = sys.stdin.readline().split()
        if len(line)==1:
            return
        print

if __name__ == '__main__':
    main()
=======
import sys
WINS = [["paper","rock"],["rock","scissors"],["scissors","paper"]]

def main():
    line = sys.stdin.readline().split()
    while (True):

        n = int(line[0])
        k = int(line[1])

        total_games = int((k*n*(n-1))/2.0)
        play_info = [[0,0] for x in range(n)] # intialize player info list

        for i in range(total_games):
            game = sys.stdin.readline().split()
            p1 = int(game[0])
            p2 = int(game[2])
            m1 = (game[1])
            m2 = (game[3])

            if [m1,m2] in WINS:
                play_info[p1-1][0] +=1 # add wins to p1
                play_info[p2-1][1] +=1 # add loose to p2
            elif m1!=m2:
                play_info[p2-1][0] +=1 # add wins to p2
                play_info[p1-1][1] +=1 # add loose to p1

        for i in play_info:
            if i[0]+i[1] == 0:
                print "-"
            else:
                print "%.3f"% round((i[0]*1.0)/(i[0]+i[1]),3)

        line = sys.stdin.readline().split()
        if len(line)==1:
            return
        print

if __name__ == '__main__':
    main()
>>>>>>> f177bf73e7319f758524fdec06543bad31a6230d
