def solution(a, b):
    answer = 0
    if a == b:
        answer = a
    else:
        if a - b<0:
            answer = a
            for i in range(1, b-a+1):
                answer += a+i
        else:
            answer = b
            for i in range(1, a-b+1):
                answer += b+i
        
    return answer
