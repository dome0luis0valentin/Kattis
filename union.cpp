#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>


using namespace std;
class Tree{
    private:
        int* parent;
        int* rank;
    public:
        // contractor
        Tree(int n){
            parent = new int[n];
            rank = new int[n];
            for (int i=0; i<n; i++){
                parent[i] = i;
                rank[i] = 0;
            }
        }
        // destructor
        ~Tree(){
            delete [] parent;
            delete [] rank;
        }

        // find with path compression
        int find (int a){
            if (a == parent[a]){
                return a;
            }
            else{
                int p = find(parent[a]);
                parent[a] = p;
                return p;
            }
        }
        // union by rank
        void unite (int a,int b){
            int p1 = find(a);
            int p2 = find(b);
            if (p1 == p2){
                return;
            }
            if (rank[p1] > rank[p2]){
                parent[p2] = p1;
            }
            else if(rank[p1]<rank[p2]){
                parent[p1] = p2;
            }
            else{
                parent[p1] = p2;
                rank[p2]++;
            }
        }
        // checks if 2 values are in the same set
        bool same(int a, int b){
            return (find(a) == find(b));
        }
};

int main(int argc, char* argv[]){
    //ifstream in;
    //in.open(argv[1]);
    int n,m,a,b;
    cin >> n >> m;
    Tree* familiy = new Tree(n);
    string command;

    for (int i=0; i<m;i++){
        cin >> command >> a >> b;
        if (command == "="){
            familiy->unite(a,b);
        }
        else if (familiy->same(a,b)){
            cout << "yes" << endl;
        }
        else{
            cout << "no" << endl;
        }
    }
    return 0;
}
