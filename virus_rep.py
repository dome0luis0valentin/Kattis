import sys

def count(before, after):
    min_len = min(len(before),len(after))
    front_match = 0
    while (front_match < min_len and before[front_match]==after[front_match]):
        front_match +=1

    back_match = 0
    i = -1
    while(back_match < min_len and before[i]==after[i]):
        back_match +=1
        i -= 1

    return len(after)-(front_match+back_match)
def main():
    before = sys.stdin.readline().strip()
    after = sys.stdin.readline().strip()
    ans = count(before,after)
    if ans <= 0:
        print abs(len(before)-len(after))
    else:
        print ans
main()
