import sys
from collections import deque

words = set()
word_map = {}
inverse_map ={}
graph = {}
char_pos = [set() for i in xrange(16)]

def addEdges(word):
  graph[word_map[word]] = set()
  for i in xrange(len(word)):
    for new_ch in char_pos[i]:
      if (new_ch != word[i]):
        neighbor = word[0:i]+new_ch+word[i+1:]
        # if possible neighbor is actual neighbor, add an edge (undirected)
        if neighbor in words:
          graph[word_map[neighbor]].add(word_map[word])
          graph[word_map[word]].add(word_map[neighbor])

def bfs(source, dest, v_count):
  visited = [False for i in xrange(v_count)]
  prev = [-1 for i in xrange(v_count)] # p_i is prev_v in path from source to v_i
  dist = [-1 for i in xrange(v_count)] # d_i is distance from source for v_i

  visited[source] = True
  prev[source] = source
  dist[source] = 0

  q = deque([source])
  while len(q) > 0:
    u = q.popleft()
    for neighbor in graph[u]:
      if not visited[neighbor]:
        visited[neighbor] = True
        q.append(neighbor)
        dist[neighbor] = dist[u] + 1
        prev[neighbor] = u
        if neighbor == dest:
          v = dest
          path = deque([v])
          while v!=source:
            v = prev[v]
            path.append(v)
          return dist[dest],path
  return dist[dest],deque([dest])

def main():
  # Collect the words
  word = sys.stdin.readline().strip()
  curr=1
  while word != "":
    if word not in words:
      word_map[word] = curr
      inverse_map[curr] = word
      curr += 1

    addEdges(word)
    # Add char_pos info
    pos = 0
    for ch in word:
      char_pos[pos].add(ch)
      pos += 1
    words.add(word)
    word = sys.stdin.readline().strip()

  # Now look for shortest paths
  prev_line = False
  for line in sys.stdin:
    source, dest= line.split()
    s,d = word_map[source], word_map[dest]
    dist,path = bfs(s,d,curr)
    if prev_line:
      print
    if dist == -1:
      print "No solution."
    else:
      while len(path) > 0:
        print inverse_map[path.pop()]
    prev_line = True

if __name__ == '__main__':
   main()
