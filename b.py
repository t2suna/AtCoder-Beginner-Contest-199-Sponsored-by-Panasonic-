import sys

N = int(input())
list_a = list(map(int,input().split()))
list_b = list(map(int,input().split()))

list_n = []

for i in range(list_b[0] - list_a[0] + 1):
    list_n.append(i+list_a[0])

for i in range(N-1):
    if(list_a[i+1] > list_n[0]):
        for j in range(list_a[i+1] - list_n[0]):
            try:            
                list_n.pop(0)
            except IndexError:
                print(0)
                sys.exit()
    if(list_b[i+1] < list_n[len(list_n)-1]):
        for j in range(list_n[len(list_n)-1] - list_b[i+1]):
            try:            
                list_n.pop(len(list_n)-1)
            except IndexError:
                print(0)
                sys.exit()
#print(list_n)
print(len(list_n))