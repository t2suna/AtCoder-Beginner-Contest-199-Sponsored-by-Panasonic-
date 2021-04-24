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
