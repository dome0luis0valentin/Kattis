#include <iostream>
#include <unordered_set>
#include <bitset>

using namespace std;

int main(){
  int X, Y, n, qx, qy;
  bitset<40000> ld,rd,col,firstX,part;
  bitset<20000> row;
  cin >> X >> Y >> n;
  while (X+Y+n){
    ld.set(); rd.set(); col.set(); row.set();
    for (int i=0; i<n; i++){
      cin >> qx >> qy;
      qx --; qy--;
      col[qx] = false;
      row[qy] = false;
      ld[qx+qy] = false;
      rd[Y-1+qx-qy] = false;
    }
    firstX.set(); part.set();
    part>>(40000-(X+Y-1));
    firstX>>=(40000-X);

    ld &= part; rd &=part;
    int total = 0;
    col &= firstX;

    for (int y=0; y<Y; y++){
      if (row[y])
        total += (col & ld & (rd >> (Y-1))).count();
      ld>>=1; rd<<=1;
    }
    cout << total << endl;
    cin >> X >> Y >> n;
  }
}


