<<<<<<< HEAD
import sys
import math

def choose(a,b):
    # a!/(b!(a-b)!)
    return math.factorial(a)/(math.factorial(b)*math.factorial(a-b))

def split_tree(tree):
    a=[]
    b=[]
    pivot = int(tree[0])
    for i in range(1,len(tree)):
        if pivot>int(tree[i]):
            a.append(tree[i])
        else:
            b.append(tree[i])

    return a,b

def count_perm(tree):
    if len(tree) == 0 :
        return 1
    a,b = split_tree(tree)
    o1 = count_perm(a)
    o2 = count_perm(b)

    return o2*(o1)*choose(len(tree)-1,len(b))

def main():
    n = int(sys.stdin.readline().strip())
    while (n!=0):
        tree = sys.stdin.readline().strip().split()
        print (int(count_perm(tree)))
        n = int(sys.stdin.readline().strip())

# def main():
#     f = open(sys.argv[1],"r")
#     n = int(f.readline().strip())
#     while (n!=0):
#         tree = f.readline().strip().split()
#         print (int(count_perm(tree)))
#         n = int(f.readline().strip())



if __name__ == '__main__':
    main()
=======
import sys
import math

def choose(a,b):
    # a!/(b!(a-b)!)
    return math.factorial(a)/(math.factorial(b)*math.factorial(a-b))

def split_tree(tree):
    a=[]
    b=[]
    pivot = int(tree[0])
    for i in range(1,len(tree)):
        if pivot>int(tree[i]):
            a.append(tree[i])
        else:
            b.append(tree[i])

    return a,b

def count_perm(tree):
    if len(tree) == 0 :
        return 1
    a,b = split_tree(tree)
    o1 = count_perm(a)
    o2 = count_perm(b)

    return o2*(o1)*choose(len(tree)-1,len(b))

def main():
    n = int(sys.stdin.readline().strip())
    while (n!=0):
        tree = sys.stdin.readline().strip().split()
        print (int(count_perm(tree)))
        n = int(sys.stdin.readline().strip())

# def main():
#     f = open(sys.argv[1],"r")
#     n = int(f.readline().strip())
#     while (n!=0):
#         tree = f.readline().strip().split()
#         print (int(count_perm(tree)))
#         n = int(f.readline().strip())



if __name__ == '__main__':
    main()
>>>>>>> f177bf73e7319f758524fdec06543bad31a6230d
