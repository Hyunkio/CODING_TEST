def solution(array, commands):
    answer = []
    
    for command in commands:
        i, j, k = command[0], command[1], command[2]
        
        num_Arr = array[i-1:j]
        num_Arr.sort()
        answer.append(num_Arr[k-1])
        
    return answer