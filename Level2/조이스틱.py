def solution(name):
    list = [min(ord(s) - ord('A'), ord('Z') - ord(s) + 1) for s in name]
    
    answer = 0
    locat = 0

    while 1:

        answer += list[locat]

        list[locat] = 0

        if sum(list) == 0: break
        
        left = 1
        right = 1

        while list[locat + right] == 0:
            right += 1

        while list[locat - left] == 0:
            left += 1
            
        if left >= right:
            locat += right
            answer += right

        else:
            locat -= left
            answer += left

    return answer
