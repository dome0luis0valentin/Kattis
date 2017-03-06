import sys

class Matrix:
    """
    A 3x3 Matrix, with a special flip method
    """
    def __init__(self,array):
        row  = ()
        for i in range(len(array)):
            array[i] = tuple(array[i])
        self.data = tuple(array)

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

    def neighbours(self,prev):
        neigh = set([])
        count = 0
        for i in range(3):
            for j in range(3):
                flipped = self.flip(i,j)
                neigh.add(flipped)
                if flipped in prev:
                    count += 1
        return neigh,count == 9



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

def solve(start):
    steps = 0

    all_prev = set([start])

    curr_lvl = set([start])

    while (ZERO not in curr_lvl):
        next_lvl = set()
        really_end = 0
        for i in curr_lvl:
            nine_flipped, end = i.neighbours(all_prev)
            next_lvl.update(nine_flipped)
            if end:
                really_end += 1

        if really_end == len(curr_lvl):
            return -1
        curr_lvl = next_lvl
        all_prev.update(curr_lvl)
        steps +=1
    return steps

def main():
    import time
    start_time = time.time()
    a = []
    for line in sys.stdin:
        line = [int(i) for i in line.split()]
        a.append(line)

    start = Matrix(a)
    print solve(start)
    print "Total time taken",time.time()-start_time,"seconds"



if __name__ == '__main__':
    main()
