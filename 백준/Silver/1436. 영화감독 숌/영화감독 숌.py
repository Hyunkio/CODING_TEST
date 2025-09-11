import sys

def triple_Six():
    n = int(sys.stdin.readline())

    count = 0
    end_Six = 665

    while True:
        end_Six += 1
    
        if '666' in str(end_Six):
            count += 1
        
        if count == n:
            print(end_Six)
            break

triple_Six()