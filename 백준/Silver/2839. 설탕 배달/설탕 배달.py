import sys

def sugar_Drive(): #3kg, 5kg
    n = int(sys.stdin.readline())
    
    for i in range(n // 5, -1, -1):
        kg_Count = n - (i * 5)
        
        if kg_Count % 3 == 0:
            j = kg_Count // 3
            print(i + j)
            return
    print(-1)

sugar_Drive()    