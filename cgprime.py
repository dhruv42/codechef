from math import sqrt
def nthprime(n):
    prime=[]
    p=[True]*(n+1)
    p[0]=p[1]=False
    for i in range(2,n+1):
        if p[i]==True:
            prime.append(i)
            for j in range(i*i,n+1,i):
                p[j]=False
    return prime

cases = int(input())
result = nthprime(1000000)
while cases>0:
    k = int(input())
    print result[k-1]
    cases-=1