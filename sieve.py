import sys

def main():
    f = open(sys.argv[1],"w")
    primes = sieve(int(sys.argv[2]))
    f.write("{")
    for i in primes:
        f.write(str(i)+",")
    f.write("}")
    f.close()
    print "Done!"

if __name__ == '__main__':
    main()
