import sys
HEX_MAP = {"0":0,"1":1,"2":2,"3":3,"4":4, "5":5, "6":6, "7":7, "8":8, "9":9,
            "a":10,"b":11, "c":12, "d":13, "e":14, "f":15,
            "A":10,"B":11, "C":12, "D":13, "E":14, "F":15}

def deci(hex_num):
    hex_str = hex_num
    hex_num = hex_num[2:]
    total = 0
    power = len(hex_num) -1
    for i in hex_num:
        total += HEX_MAP[i] *(16 ** power)
        power -= 1
    print hex_str,total

def main():
    f=open("sample.in","r")
    for line in f:
        hex_init = ""
        cur = ""
        last =""
        started = False

        for i in line:
            cur = i
            if not started:
                hex_init = last+cur
                if  hex_init == "0x" or  hex_init == "0X":
                    started = True
            elif started:
                if i not in HEX_MAP or len(hex_init)>9:
                    started = False
                    if len(hex_init) > 2:
                        deci(hex_init)
                    cur = " "
                else:
                    hex_init += i
            last = cur




main()
