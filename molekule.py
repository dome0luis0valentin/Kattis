import sys

def main():
    #f = open(sys.argv[1],"r")
    graph = {}
    next(sys.stdin)
    for line in sys.stdin:
        switch = False
        line = [int(i) for i in line.split()]
        if line[0] not in graph:
            if line[1] not in graph:
                graph[line[0]] = 0
                graph[line[1]] = 1
            else:
                if graph[line[1]] == 1:
                    graph[line[0]] = 0
                else:
                    graph[line[0]] = 1
                    switch = True
        else: # first molecule already has designated position
            if line[1] not in graph:
                if graph[line[0]] == 0:
                    graph[line[1]] = 1
                else:
                    graph[line[1]] = 0
                    switch = True
            else:
                p1 = graph[line[0]]
                p2 = graph[line[1]]
                if  p1!= p2:
                    if p1 == 1:
                        switch = True

        if switch:
            print 1
        else:
            print 0

if __name__ == '__main__':
    main()
