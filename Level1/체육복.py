def solution(n, lost, reserve):
    answer = n - len(lost)
    for i in range(len(lost)):
        if lost[i] in reserve:
            del reserve[reserve.index(lost[i])]
            lost[i] = -1
            answer+=1
    for i in range(len(lost)):
        if lost[i] == -1:
            continue
        elif lost[i]-1 in reserve:
            del reserve[reserve.index(lost[i]-1)]
            answer += 1
        elif lost[i]+1 in reserve:
            del reserve[reserve.index(lost[i]+1)]
            answer += 1
            
    

    return answer
