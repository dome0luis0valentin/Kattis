import sys
MD ={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
YEAR_RANGE = range(2000,3000,100)
def is_leap(year):
    year = int(year)
    if year % 4 == 0 :
        if (((year % 100) == 0) and ((year % 400)!=0)):
            MD[2] = 28
            return False
        MD[2] = 29
        return True
    MD[2] = 28
    return False
def validate(y,m,d):
    if (len(str(m))==4) or len(str(d)) == 4:
        return False
    if len(str(y)) == 4:
        is_leap(y)
        if (2000<= y <= 2999) and (1<= m <= 12) and (1<= d <= MD[m]):
            if len(str(m)) == 1:
                m = "0"+str(m)
            if len(str(d)) == 1:
                d = "0"+str(d)
            print str(y)+"-"+str(m)+"-"+str(d)
            return True
        else:
            return False

    for i in YEAR_RANGE:
        year = i + y
        is_leap(year)
        if (2000<= year <= 2999) and (1<= m <= 12) and (1<= d <= MD[m]):
            if len(str(m)) == 1:
                m = "0"+str(m)
            if len(str(d)) == 1:
                d = "0"+str(d)
            print str(year)+"-"+str(m)+"-"+str(d)
            return True
    return False


def main():
    #f = open(sys.argv[1],"r")
    line = sys.stdin.readline().strip()
    date = line.split("/")
    for i in range(3):
        date[i] = int(date[i])

    date.sort()
    a = date[0]
    b = date[1]
    c = date[2]
    all_perms= [[a,b,c],[a,c,b],[b,a,c],[b,c,a],[c,a,b],[c,b,a]]

    for i in all_perms:
        if validate(*i):
            return

    print line, "is illegal"
    return

if __name__ == '__main__':
    main()
