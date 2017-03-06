import sys,math

def main():
    while True:
        key = int(sys.stdin.readline().strip())
        if key == 0:
            return
        plain_txt = sys.stdin.readline().strip().replace(" ","")
        cipher = [""]*len(plain_txt)

        i = 0
        for offset in range(key):
            index = offset
            while index < len(plain_txt):
                cipher[index] = plain_txt[i].upper()
                index += key
                i +=1
        print "".join(cipher)

if __name__ == '__main__':
    main()
