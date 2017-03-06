#include <iostream>
#include <vector>
#include <list>
#include <queue>
#include <string>
#include <algorithm>
#include <set>
#include <climits>

using namespace std;

// The following will be used in the priority queue for Dijkstra's Algorithm
struct Edge{
    int dist,weight; // destination and weight
    Edge(int d){
        dist = d;
        weight = INT_MAX;
    }
    Edge(int d,int w){
        dist = d; weight = w;
    }
    bool operator < (Edge other) const{
        return weight > other.weight;
    }
};

class Graph{

    public:
      // constructor
      Graph(int n,int m): edgeCount(m), vertixCount(n) {
          vertices(n);
      }
      virtual ~Graph(){}

      void addEdge(int v1, int v2, int w){
          vertices[v1].push_back(Edge(v2,w));
      }

      void path(int* distance,int src){
          priority_queue<Edge> pq;

          distance[src] = 0;
          pq.push(Edge(src,0));

          list<Edge> neighbors;
          list<Edge>::iterator iter;

          int curr,w,u,u_w;
          while (!pq.empty()){
              curr = pq.top().dist;
              w = pq.top().weight;
              pq.pop();
              neighbors  = vertices[curr];

              for (iter = neighbors.begin(); iter!=neighbors.end(); iter++){
                  u = (*iter).dist;
                  u_w = (*iter).weight;
                  if (distance[u] > w + u_w){
                      distance[u] = w + u_w;
                      pq.push(Edge(u,distance[u]));
                  }
              }
          }
      }

    private:
      int edgeCount;
      int vertixCount;
      vector<list<Edge> > vertices;

};

int main(){
    int n,m,q,s;
    int u,v,w;
    int query;
    while (true){
        cin >> n >> m >> q >> s;
        if (!n) break;
        Graph network = Graph(n,m);
        for (int i=0; i<m;i++){
            cin >> u >> v >> w;
            network.addEdge(u,v,w);
        }
        int* distance = new int[n];
        fill_n(distance,n,INT_MAX);
        network.path(distance,s);
        for (int j=0; j<q;j++){
            cin>>query;
            if (distance[query] == INT_MAX) cout<<"Impossible"<<endl;
            else cout << distance[query]<<endl;
        }
        cout <<endl;
    }
}
