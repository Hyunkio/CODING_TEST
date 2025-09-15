import sys

def coordinate():
    result= []    
    n = int(sys.stdin.readline())
    
    for _ in range(n):
        x, y = list(map(int, sys.stdin.readline().split()))
        result.append((x, y))
        
    result.sort()
    
    for x, y in result:
        print(x, y)

coordinate()
        