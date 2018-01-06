import sys

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class FIFO:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self,data):
        a_node = Node(data)
        if self.head == None:
            self.head = a_node
            self.tail = a_node
        else:
            self.tail.next = a_node
            self.tail = a_node

    def peek(self):
        return self.head.data if self.head!=None else None

    def pop(self):
        if self.head != None:
            val = self.head.data
            self.head = self.head.next
            return val
        else:
            return None
    def empty(self):
        return self.head==None

    def __repr__(self):
        # expensive method - should use only for debug
        rep_str = []
        curr_node = self.head
        while(curr_node != None):
            rep_str.append(str(curr_node.data))
            curr_node = curr_node.next
        return " ".join(rep_str)

def main():
    cases = int(sys.stdin.readline().strip())
    for i in xrange(cases):
        n,m,l = [int(i) for i in sys.stdin.readline().split()]
        graph = {}
        for j in xrange(m):
            x,y = [int(i) for i in sys.stdin.readline().split()]
            if x not in graph:
                graph[x] = [y]
            else:
                graph[x].append(y)
        # bfs

        visited = [False for k in xrange(n)]
        q = FIFO()
        for i in xrange(l):
            q.push(int(sys.stdin.readline().strip()))
            count = 0
            while(not q.empty()):
                curr = q.pop()
                visited[curr-1] = True
                if (curr in graph):
                    for neighbor in graph[curr]:
                        if not visited[neighbor-1]:
                            q.push(neighbor)

        print sum(visited)

if __name__ == '__main__':
    main()
