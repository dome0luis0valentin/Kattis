"""
Building the graph takes way too long
"""
import sys
import Queue as Q
class Vertex:
    def __init__(self,key,i):
        self.key = key # ususally the weight to get to that vertex
        self.id = i

    def __ge__(self,other):
        return self.key > other.key
    def __eq__(self,other):
        return (self.key,self.id) == (other.key,other.id)
    def __ne__(self,other):
        return not self.__eq__(other)
    def __hash__(self):
        return hash((self.id, self.key))

    def __str__(self):
        return str((self.id, self.key))

class Graph:
    def __init__(self):
        self.ids = 0 # number of vertices
        self.data={} # adjacency list

    def neighbors(self,vid):
        return self.data[vid]

    def addVertex(self,key):
        v = Vertex(key,self.ids)
        self.data[v] = []
        self.ids +=1
        return v

    def addEdge(self,v1,v2):
        self.data[v1].append(v2)

    def path(self,v1, v2):
        pred = [-1 for i in range(self.ids)]  # to recover path
        # initalize distance array
        d = [-1 for i in range(self.ids)]
        pq = Q.PriorityQueue()
        d[v1.id] = v1.key
        pq.put((d[v1.id],v1)) # priority queue based on distance from v1
        gotWhereIwant = False

        while(not pq.empty() and (not gotWhereIwant)):
            v = pq.get()[1]

            for n in self.data[v]:
                if d[n.id] == -1 or ((d[v.id] + n.key) < d[n.id]):
                    d[n.id] = d[v.id] + n.key
                    pred[n.id] = v
                    pq.put((d[n.id],n))
                if n == v2:
                    gotWhereIwant = True
                    break
        # pred can be used to recover path
        return d[v2.id]

class Matrix:
    """
    A 3x3 Matrix, with a special flip method
    """
    def __init__(self,array):
        if type(array[0]) == type([]):
            for i in range(len(array)):
                array[i] = tuple(array[i])
                self.data = tuple(array)
        elif type(array[0]) == type(""):
            table = []
            for i in array:
                row = tuple([int(k) for k in i])
                table.append(row)
            self.data = tuple(table)


    def flip(self,i,j):
        new_mat = []
        for row in range(3):
            a_row = []
            for col in range(3):
                if col == j or row == i:
                    a_row.append((self.data[row][col]+1)%4)
                else:
                    a_row.append(self.data[row][col])
            new_mat.append(a_row)
        return Matrix(new_mat)

    def __repr__(self):
        str_rep = ""
        for i in self.data:
            for j in i:
                str_rep += str(j)+" "
            str_rep = str_rep.strip()
            str_rep += "\n"
        return str_rep

    def __eq__(self,other):
        return self.data == other.data
    def __ne__(self,other):
        return not self.__eq__(other)
    def __hash__(self):
        return hash(self.data)

ZERO = Matrix([[0,0,0],[0,0,0],[0,0,0]])

def permutation(n,a_str):
    if n==1:
        return list(a_str)

    less_perm = permutation(n-1,a_str)
    final = []
    for i in less_perm:
        for j in a_str:
            final.append(j+i)
    return final



def main():

    m_v = {}

    poss_rows = permutation(3,"0123")
    solution_graph = Graph()

    weight = 1
    for first in poss_rows:
        for second in poss_rows:
            for third in poss_rows:
                a_mat = Matrix([first,second,third])
                v = solution_graph.addVertex(weight)
                m_v[a_mat] = v

    for matrix in m_v:
        for r in range(3):
            for c in range(3):
                new = matrix.flip(r,c)
                solution_graph.addEdge(m_v[matrix],m_v[new])

    a = []
    for line in sys.stdin:
        line = [int(num) for num in line.split()]
        a.append(line)
    start = Matrix(a)
    print "Looking for path"
    print solution_graph.path(m_v[start],m_v[ZERO])

if __name__ == '__main__':
    main()
