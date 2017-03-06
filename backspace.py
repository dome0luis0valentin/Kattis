import sys

def main():
    code = sys.stdin.readline().strip()
    ans = [] 
    for i in code:
        if i != "<":
            ans.append(i)
        else:
            ans.pop()
    print "".join(ans)

if __name__ == "__main__":
    main()