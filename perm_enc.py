import sys
def encrypt_part(msg,key):
    final = ""
    for i in key:
        final+= msg[int(i)-1]
    return final

def encrypt(msg,key):
    keyLength = len(key)
    msgLength = len(msg)
    if msgLength % keyLength != 0: # pad message
        msg += " "*(keyLength - (msgLength % keyLength))

    encrypted = ""
    for i in range(0,len(msg),keyLength):
        encrypted += encrypt_part(msg[i:i+keyLength],key)

    return "\'"+encrypted+"\'"

def main():
    i=0
    for line in sys.stdin:
        if i%2 == 0:
            key = line.strip().split()[1:]
        else:
            message = line.strip()
            print encrypt(message,key)
        i+=1
if __name__ == "__main__":
    main()
