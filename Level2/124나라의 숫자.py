def solution(n):
    answer = ''
    while (n>3):
        if n % 3 == 0:
            answer += str(4)
            n = n//3 - 1
        else:
            answer += str(n%3)
            n = n//3
    if n==1 or n==2:
        answer+=str(n)
    else:
        answer+=str(4)
    answer = list(answer)
    answer.reverse()
    answer = ''.join(answer)
    return answer

