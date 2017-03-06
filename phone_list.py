import sys

class Node:
    def __init__(self,data,c = 0):
        self.data = data
        self.path = True
        self.next_p = {}
    def destination(self):
        self.path = False
    def find(self,i):
        if i in self.next_p:
            return self.next_p[i]
        return None

class Tree:
    def __init__(self):
        self.root = Node("")
    def extend(self, num):
        return self._extend(num,self.root)
    def _extend(self,num,p):
        first = num[0]
        f_node = p.find(first)
        if len(num) == 1:
            if f_node == None:
                f_node = Node(num)
                f_node.destination()
                p.next_p[first] = f_node
                return p.path
            else:
                f_node.destination()
                return False


        if f_node == None:
            f_node = Node(first)
            p.next_p[first] = f_node


        return p.path and self._extend(num[1:],f_node)

def main():
    #f = open(sys.argv[1],"r")
    cases = int(sys.stdin.readline().strip())
    for i in range(cases):
        phonebook = Tree()
        n = int(sys.stdin.readline().strip())
        flag = False
        for j in range(n):
            num = sys.stdin.readline().strip()
            if flag:
                continue
            if not phonebook.extend(num):
                flag = True


        if flag:
            print "NO"
        else:
            print "YES"

if __name__ == '__main__':
    main()
