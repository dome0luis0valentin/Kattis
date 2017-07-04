import sys

def count_changes(name):
    if len(name)==0:
        return 0
    if name[0]==name[-1]:
        return count_changes(name[1:-1])
    return 1+count_changes(name[1:-1])

def main():
    #f = open(sys.argv[1])
    name = sys.stdin.readline().strip()
    half = len(name)/2
    val = count_changes(name)
    for i in range(1,half):
        name = name[1:]
        a = count_changes(name)+i
        if val > a:
            val = a

    print val
if __name__ == '__main__':
    main()
