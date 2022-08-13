ar=list(map(int,input().split()))
n=len(ar)
l=[]

for i in range(n):
    for j in range(i+1,n):
        area=(j-i)*(min(ar[i],ar[j]))
        l.append(area)
print(max(l))
