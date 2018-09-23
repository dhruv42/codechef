cases = int(input())
while cases>0:
    a = raw_input()
    b = raw_input()
    if sorted(a)==sorted(b):
        print "Arjun"
    else:
        print "Amit"
    cases-=1