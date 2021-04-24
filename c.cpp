#include <string>       // ヘッダファイルインクルード
#include <iostream>
using namespace std;

int main() {
  int N,Q,T,A,B;
  string S;
  cin >> N;
  cin >> S;
  cin >> Q;
  for(int i=0;i<Q;i++){
      cin >> T >> A >> B;
      if(T == 1){
        string Temp(S); 
        S[A-1] = Temp[B-1];
        S[B-1] = Temp[A-1];
      }
      else if(T == 2){
        S = S.substr(N,N) + S.substr(0,N) ;
      }
  }
  cout << S;
}

/*
import cython

cdef:
    int N,Q,T,A,B
    list S
N = int(input())
S = list(input())
Q = int(input())
for i in range(Q):
    T,A,B = map(int,input().split())
    if(T==1):
        Temp = S[A-1]
        S[A-1] = S[B-1]
        S[B-1] = Temp
    elif(T==2):
        S = S[N:]+S[:N]
print("".join(S))
*/