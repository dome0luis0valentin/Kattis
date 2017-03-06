import sys

def val_weights():
    values = {}
    weight = 1
    for i in range(3,7):
        for j in range(1,i):
            values[(str(i)+str(j))] = weight
            values[(str(j)+str(i))] = weight
            weight +=1

    for i in range(1,7):
        values[str(i)+str(i)] = weight
        weight +=1
    values["21"] = weight
    values["12"] = weight
    return values

val_map = val_weights()
def poss_val(roll):
    if roll == "**":
        return val_map.keys()
    elif roll[0] == "*":
        poss = []
        for i in range(1,7):
            poss.append(str(i)+roll[1])
        return poss
    elif roll[1] == "*":
        poss = []
        for i in range(1,7):
            poss.append(roll[0]+str(i))
        return poss
    return [roll]

def gcd(a,b):
    if a == b:
        return a
    if a == 0:
        return b
    if b == 0:
        return a
    if ~a & 1:
        if b&1:
            return gcd(a>>1,b)
        else:
            return gcd(a>>1,b>>1)<<1
    if ~b & 1:
        return gcd(a,b>>1)
    if (a>b):
        return gcd((a-b)>>1,b)
    return gcd((b-a)>>1,a)

def main():
    #f = open(sys.argv[1],"r")
    for play in sys.stdin:
        if play.strip() == "0 0 0 0":
            break
        play = play.split()
        p1 = play[0]+play[1]
        p2 = play[2]+play[3]
        p1_poss = poss_val(p1)
        p2_poss = poss_val(p2)
        total = len(p1_poss)*len(p2_poss)
        wins = 0
        for i in p1_poss:
            for j in p2_poss:
                if val_map[i] > val_map[j]:
                    wins +=1


        hcf = gcd(wins,total)
        wins,total = wins/hcf, total/hcf
        if total == 1:
            print wins
        else:
            print str(wins)+"/"+str(total)


if __name__ == '__main__':
    main()
