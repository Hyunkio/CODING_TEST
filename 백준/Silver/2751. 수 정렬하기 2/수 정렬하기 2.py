import sys

def sort_Num():
    result = []
    n = int(sys.stdin.readline())
    
    for i in range(n):
        result_Num = int(sys.stdin.readline())
        result.append(result_Num)
    
    result.sort()
    
    for i in range(n):
        print(result[i])

sort_Num()