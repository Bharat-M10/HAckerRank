n=int(input())

arr=[]

for i in range(n):

    arr.append(list(map(int,input().split())))

d1=arr[0][0]

d2=arr[0][n-1]

for i in range(1,n):

    d1+=arr[i][i]

    d2+=arr[i][(n-1)-i]

print(abs(d1-d2))

​
