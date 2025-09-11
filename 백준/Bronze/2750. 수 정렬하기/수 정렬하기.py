import sys

def sort_Asc():
    n = int(sys.stdin.readline())
    arr_Num = []
    
    for i in range(n):
        num = int(sys.stdin.readline())
        arr_Num.append(num)
        
    arr_Num.sort()
    
    for num in arr_Num:
        print(num)
    
sort_Asc()