import sys
def min_product(x,y):
    for i in range(len(x)):
        x[i] = int(x[i])
        y[i] = int(y[i])

    x.sort()
    y.sort(reverse=True)

    min_sum =0
    for i in range(len(x)):
        min_sum += x[i]*y[i]
    return min_sum

def main():
    next(sys.stdin)
    counter = 0
    case_num = 1
    for line in sys.stdin:
        if counter % 3 == 1:
            x = line.strip().split()
        elif counter % 3 ==2:
            y = line.strip().split()
            print "Case #"+str(case_num)+":", min_product(x,y)
            case_num +=1
        counter +=1
if __name__ == "__main__":
    main()
