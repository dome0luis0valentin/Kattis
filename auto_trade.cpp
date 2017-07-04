<<<<<<< HEAD
#include <iostream>
#include <string>
#include <fstream>
#include <cstdlib>
using namespace std;
int count(string s, int a, int b){
    int c = 0;
    int length = s.length();
    while((b+c < length) && (s[a+c] == s[b+c])){
        c++;
    }
    return c;
}
int main(int argc, char* argv[]){
    //ifstream in;
    //in.open(argv[1]);

    int a,b;
    string s;
    cin >> s;
    cin >> a; // dont need it - thus ignored
    while(cin>>a>>b){
        cout <<count(s,a,b)<<endl;
    }
    return 0;
}
=======
#include <iostream>
#include <string>
#include <fstream>
#include <cstdlib>
using namespace std;
int count(string s, int a, int b){
    int c = 0;
    int length = s.length();
    while((b+c < length) && (s[a+c] == s[b+c])){
        c++;
    }
    return c;
}
int main(int argc, char* argv[]){
    //ifstream in;
    //in.open(argv[1]);

    int a,b;
    string s;
    cin >> s;
    cin >> a; // dont need it - thus ignored
    while(cin>>a>>b){
        cout <<count(s,a,b)<<endl;
    }
    return 0;
}
>>>>>>> f177bf73e7319f758524fdec06543bad31a6230d
