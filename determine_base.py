import sys

MAX_INT = 2**32 -1
MIN_INT = 1

def base(num, b):
    if(b==1): # won't be more that 1000
        total = len(num)
        return total, num == "1"*total
    num = str(num).lower()
    total = 0
    power = len(num)-1
    for i in num:
        if i.isdigit():
            total += (int(i)*(b**power))
        else:
            total += ((ord(i)-87)*(b**power))
        power -=1
    return total, MIN_INT <= total <= MAX_INT
def show(a_list):
    if len(a_list)==0:
        return "invalid"

    final_str = ""
    for i in a_list:
        if int(i) == 36:
            value = "0"
        elif int(i)>=10 :
            value = chr(int(i)+87)
        else:
            value = str(i)

        final_str += value

    return final_str
def main():
    sys.stdin.readline()

    for exp in sys.stdin:
        exp = exp.strip().split()
        x = exp[0]
        y = exp[2]
        z = exp[4]
        min_base = max(list(x+y+z))
        if not min_base.isdigit(): # if min base is not a number make it one
            min_base = ord(min_base.lower())-87
        min_base = int(min_base)
        if min_base != 1:
            min_base = min_base + 1 # minimum possible base

        base_that_work = []

        for i in range(min_base,37):
            a,f1 = base(x,i)
            b,f2 = base(y,i)
            c,f3 = base(z,i)
            if (f1 and f2 and f3):
                if exp[1] == "+":
                    if a + b == c:
                        base_that_work.append(i)
                elif exp[1] == "-":
                    if a - b == c:
                        base_that_work.append(i)
                elif exp[1] == "*":
                    if a * b == c:
                        base_that_work.append(i)
                elif exp[1] == "/":
                    if a*1.0/b == c*1.0:
                        base_that_work.append(i)
        print show(base_that_work)
main()
