import sys

def main():
    counter = 1
    for line in sys.stdin:
        if line.strip() != "END":
            line = line.strip()[1:-1].split("*")
            length = len(line[0])
            evenly_spaced = True
            for i in line:
                if len(i)!= length:
                    evenly_spaced = False
                    break
            if evenly_spaced:
                print counter,"EVEN"
            else:
                print counter,"NOT EVEN"
            counter +=1

if __name__ == "__main__":
    main()
