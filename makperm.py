cases = int(input())
while cases>0:
    n = int(input())
    a = map(int,raw_input().split())[:n]
    b=range(1,n+1)
    print len(list(set(b)-set(a)))
    cases-=1