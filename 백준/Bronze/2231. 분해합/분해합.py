import sys

def divide_Sum():
    
    n = int(sys.stdin.readline())
    
    for i in range(1, n+1): #1 ~ 257
        current_Sum = i + sum(map(int, str(i))) # 1 + 
        
        if current_Sum == n:
            print(i)
            return 
        
    print(0)
    
divide_Sum()