import sys
import math

def is_prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True
def get_next_prime(n):
    num = 2*n + 1
    while not is_prime(num):
        num +=2
    return num

def main():

    for line in sys.stdin:
        n = int(line.strip())
        if n!=0:
            next_prime = get_next_prime(n)
            if is_prime(n):
                print next_prime
            else:
                print next_prime,"("+str(n)+" is not prime)"



if __name__ == "__main__":
    main()
