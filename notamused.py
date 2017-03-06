import sys

log = sys.stdin.readlines() # list of strings

def computePrice(a_list):
    total = 0
    i = 0
    while i<len(a_list):
        total += (a_list[i+1] - a_list[i])
        i+=2
    return total *0.1

day_count = 0
for i in log:
    if i.strip() == "OPEN":
        log_dict = {}
        day_count += 1

    elif i.strip() == "CLOSE":
        print "Day",day_count
        names = sorted(log_dict.keys())
        for j in names:
            print j,"$" + "{0:.2f}".format(computePrice(log_dict[j]))
        print
    else:
        i = i.split() # list that looks like  ['ENTER', '***' ,'**']
        n = i[1].strip()
        if n in log_dict:
            log_dict[n].append(int(i[2].strip()))
        else:
            log_dict[n] = [int(i[2].strip())]
