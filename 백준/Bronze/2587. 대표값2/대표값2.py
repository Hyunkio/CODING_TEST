import sys

result = []

def median():
    for _ in range(5):
        n = int(sys.stdin.readline())
        result.append(n)
        
    avg = sum(result) // 5
    result.sort()
    middle = result[2]
    
    print(avg)
    print(middle)
    
median()