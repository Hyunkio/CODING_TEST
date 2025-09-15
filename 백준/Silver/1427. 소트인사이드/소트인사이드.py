import sys

def arr_Desc():
    n = sys.stdin.readline()
    descent_Num = list(n)
        
    descent_Num.sort(reverse = True)
    
    print("".join(descent_Num))
    
arr_Desc()