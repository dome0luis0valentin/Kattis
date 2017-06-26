import sys

def count(s1,s2):
    c = 0
    length = len(s2)
    while (c<length and (s1[c] == s2[c])):
        c += 1
    return c

def main():
    f= open(sys.argv[1],"r")
    s = f.readline().strip()
    next(f) # skip the next line
    for line in f:
        line = line.split()
        start1 = int(line[0])
        start2 = int(line[1])
        print count(s[start1:],s[start2:])

if __name__ == '__main__':
    main()
