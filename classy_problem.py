import sys
MAP = {'upper':'3','lower':'1', 'middle':'2'}
class Classy:
    def __init__(self,name,c):
        self.name = name
        self.c = ""
        length = len(c)
        for i in range(length):
            self.c += MAP[c[length-1-i]] # reverse order
    def __gt__(self,c2):
        s1 = self.c
        s2 = c2.c
        while (len(s1)!=len(s2)):
            if len(s1)>len(s2):
                s2 += "2"
            else:
                s1 += "2"

        if s1 == s2:
            return self.name < c2.name
        else:
            return s1 > s2

    def __str__(self):
        return self.name+": "+self.c


def main():
    cases = int(sys.stdin.readline().strip())
    for i in range(cases):
        n = int(sys.stdin.readline().strip())
        a_list = []
        for i in range(n):
            line = sys.stdin.readline().split()
            a_list.append(Classy(line[0][:-1],line[1:-1][0].split("-")))

        a_list.sort()
        for i in range(n):
            print a_list[n-1-i].name
        print "".center(30,"=")

if __name__ == '__main__':
    main()
