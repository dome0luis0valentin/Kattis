import sys

def main():
    line = sys.stdin.readline()
    line = line.strip().split()
    x = min(int(line[0]),int(line[1]))
    y = max(int(line[0]),int(line[1]))
    for i in range(x+1,y+2):
        print i

main()
