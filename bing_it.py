import sys,bisect

class Node:
    def __init__(self,data,c = 0):
        self.data = data
        self.count = c
        self.next_p = {}
    def next_to(self,i):
        return i in self.next_p



class FamilyTree:
    def __init__(self):
        self.root = Node("")
    def extend_family(self,word):
        return self._extend(self.root,word)
    def _extend(self,p,word):
        p.count +=1
        if word == "":
            return p.count-1

        first_letter = word[0]
        if p.next_to(first_letter):
            p.next_p[first_letter] = Node(first_letter)

        return self._extend(p.next_p[first_letter],word[1:])

def main():
    #f = open(sys.argv[1],"r")
    n = int(sys.stdin.readline().strip())
    tree = FamilyTree()
    for i in range(n):
        word = sys.stdin.readline().strip()
        print tree.extend_family(word)

if __name__ == '__main__':
    main()
