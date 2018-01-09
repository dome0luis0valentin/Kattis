import sys

dictionary = {}

line = sys.stdin.readline().strip()
while(line!=""):
    x,y = line.split()
    dictionary[y] = x
    line = sys.stdin.readline().strip()

for line in sys.stdin:
    line = line.strip()
    if line in dictionary:
        print dictionary[line]
    else:
        print "eh"
