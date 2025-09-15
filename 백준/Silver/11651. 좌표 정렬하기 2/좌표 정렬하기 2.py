import sys

def coordinate_Two():
    result = []
    n = int(sys.stdin.readline())
    
    for i in range(n):
        x, y = map(int, sys.stdin.readline().split())
        result.append((y, x))
        
    result.sort()
    
    for y, x in result:
        print(x, y)

coordinate_Two()
        
        