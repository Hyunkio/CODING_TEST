import sys

def blackjack():
    n, m = map(int, sys.stdin.readline().split())
    card_Num = list(map(int, sys.stdin.readline().split()))
    max_Sum = 0
    
    for i in range(n): #0~4
        for j in range(i+1, n): #1~4
            for k in range(j+1, n): #2~4
                current_Sum = card_Num[i] + card_Num[j] + card_Num[k]
                
                if current_Sum <= m and current_Sum > max_Sum:
                    max_Sum = current_Sum
                    
    print(max_Sum)
        
blackjack() 