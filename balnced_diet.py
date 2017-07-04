import sys

def find_partition(a_list):
    total = sum(a_list)
    half = (total/2) + 1
    table = [[False]*(len(a_list)+1) for i in range(half)]
    for i in range(len(a_list)):
        table[0][i] = True

    closest = 0
    for p_s in range(1,half):
        flag = False
        for i in range(1,len(a_list)+1):
            if p_s - a_list[i-1] >= 0:
                table[p_s][i] = table[p_s][i-1] or table[p_s-a_list[i-1]][i-1]
            else:
                table[p_s][i] = table[p_s][i-1]
            flag = flag or table[p_s][i]

        if flag:
            closest = p_s

    return total - closest, closest




def main():
    for line in sys.stdin:
        if line.strip() == '0':
            break
        a_list = [int(i) for i in line.split()]
        a,b = find_partition(a_list[1:])
        print a,b

if __name__ == '__main__':
    main()
