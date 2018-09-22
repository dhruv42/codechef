cases = int(input())
while cases > 0:
    n = int(input())
    if 360%(180-n)!=0:
        print "NO"
    else:
        print "YES"
    cases-=1
