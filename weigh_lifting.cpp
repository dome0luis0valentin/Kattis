#include <iostream>
#include <stdlib.h>
#include <algorithm>
#include <iomanip>

using namespace std;

int main(int argc, char * argv[]){
    int e,es,ef;
    cout << fixed;
    cout << setprecision(13);
    cin >> e >> es >> ef;
    long BIGNUM = 1000000000000;
    long *splits = (long *) malloc((e+1)*sizeof(long long));
    splits[0] = 0;
    for (int i=0; i<=e; i++){
        splits[i] = min(((i<=es)? 0:splits[i-es]) + ((i<=ef)? 0:splits[i-ef]) +1, BIGNUM);
    }

    long p = splits[e]+1;
    cout << min(225.0/p,200.0/(p-1))<<endl;
    free(splits);
    return 0;
}
