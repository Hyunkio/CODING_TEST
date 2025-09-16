import sys

def coin():
    n, k = map(int, sys.stdin.readline().split())
    coin_Arrs = []
    
    for _ in range(n):
        coin_Arrs.append(int(sys.stdin.readline()))
    
    count = 0    
    coin_Arrs.sort(reverse = True)
    
    for coin_Arr in coin_Arrs:
        num_Of_Coin = k // coin_Arr
        count += num_Of_Coin
        
        k %= coin_Arr
        
        if k == 0:
            break
    
    print(count)

coin()