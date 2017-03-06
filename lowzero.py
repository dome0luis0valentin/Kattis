import sys,time,math

def least_significant(n,intereseting):
    ans = {1:1,0:1,2:2}
    c = {0:2,1:4,2:8,3:6}  # any power of 2 end in one of these
    c_i = {2:0,4:1,8:2,6:3}
    least = 0
    for i in range(3,n+1):
        k = i
        tens = 0
        while k%5 == 0:
            k /= 5
            tens +=1

        tens = tens%4
        least = (least - tens) % 4
        val = (c[least]*k)%10

        least = c_i[val]

        if i in intereseting:
            ans[i] = val

    return ans

def main():
    max_val = 0
    #f = open(sys.argv[1],"r")

    nums = []
    for line in sys.stdin:
        n = int(line.strip())
        if n!=0:
            nums.append(n)
            if n > max_val:
                max_val = n

    ans = least_significant(max_val,set(nums))
    for i in nums:
        print ans[i]

if __name__ == '__main__':
    main()
