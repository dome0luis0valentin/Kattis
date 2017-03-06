import sys

def main():
    next(sys.stdin)
    for line in sys.stdin:
        line = line.strip().split()
        for i in range(len(line)):
            line[i] = int(line[i])
        line.sort(reverse=True)

        max_discount = 0
        for j in range(-1,len(line),3):
            if j>0:
                max_discount += line[j]

        print max_discount

main()
