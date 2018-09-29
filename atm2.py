cases = int(input())
while cases>0:
    n,k = map(int,raw_input().split())
    a = map(int,raw_input().split())[:n]
    s = ""
    for i in range(n):
        if a[i]<=k:
            s+="1"
            k-=a[i]
        else:
            s+="0"
    print s 
    cases-=1