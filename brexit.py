import sys

def remove_node(n,graph,degree,degree_original,visited,x):
    to_remove = [n]
    while len(to_remove) > 0:
        rm_node = to_remove.pop()
        visited[rm_node] = True
        for c in graph[rm_node]:
            if (not visited[c]):
                degree[c] -= 1
                if (degree[c] <= degree_original[c]/2):
                    to_remove.append(c)
        degree[rm_node] = 0
        if degree[x] <= degree_original[x]/2:
            return

def main():
    c,p,x,l = [int(i) for i in sys.stdin.readline().split()]
    graph = [[] for i in range(c+1)]
    visited = [ False for i in range(c+1) ]

    degree_original = [0 for i in range(c+1)]
    degree_count = [0 for i in range(c+1)]
    for line in sys.stdin:
        a,b = [int(j) for j in line.split()]

        graph[a].append(b)
        degree_original[a] += 1
        degree_count[a] += 1

        graph[b].append(a)
        degree_original[b] += 1
        degree_count[b] +=1

    remove_node(l,graph,degree_count,degree_original,visited,x)

    if degree_count[x] > degree_original[x]/2:
        return 'stay'
    return 'leave'

if __name__ == '__main__':
    print (main())
