import sys

def confusion(n,m):
    '''
    counts all possible seqs of length n (where the elements are all 1...n and
    unique) that have a confusion number of m.
    Look at https://open.kattis.com/problems/zbrka for more explanation
    This is just the recursive relationship - slow
    '''
    if (n==1 and m==0):
        return 1
    if (n==1 and m>0):
        return 0

    final = 0
    for i in xrange(min(n,m+1)):
        final += confusion(n-1,m-i) % 1000000007
    return final

def prev_n_sum(a_list,n,m):
    final = [0]
    reverse = []
    for i in range(m+1):
        val = a_list[i] + final[i]
        if (i>=n):
            val -= a_list[i-n]
        final.append(val % 1000000007)
    return final


def confusion_d(n,m):
    '''
    Dynamic solution based on the above recursive solution
    '''
    table = [1]+[0]*(m)
    for i in range(1,n+1):
        table = prev_n_sum(table,i,m)[1:]
    return table



def main():
    n,m = [int(x) for x in sys.stdin.readline().split()]
    #print confusion(n,m)
    print confusion_d(n,m)[-1]

if __name__ == '__main__':
    main()
