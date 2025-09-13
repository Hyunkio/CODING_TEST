import sys

def num_Asc():
    result = [0] * 10001
    n = int(sys.stdin.readline())
    
    for _ in range(n):
        result_Arr = int(sys.stdin.readline())
        result[result_Arr] += 1
    
    for i in range(1, 10001):
        if result[i] > 0:
            for _ in range(result[i]):
                print(i)
        
num_Asc()