fn0, fn1 = map(int,input().split()) 
c = int(input()) 
n0 = int(input())

if  fn0 <= c and fn0 * n0 + fn1 <= c * n0:
    print(1)
else:
    print(0)