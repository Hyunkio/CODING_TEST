import sys

def certificate():
    mem, cut = map(int, sys.stdin.readline().split())  
    score = list(map(int,sys.stdin.readline().split()))
    
    score.sort(reverse = True)
    
    print(score[cut - 1])

certificate()