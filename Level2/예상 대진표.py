#내 풀이

def solution(n,a,b):
    answer = 0
    while True:
        if (a-b==1 and a%2==0 and b%2==1) or (b-a == 1 and a%2==1 and b%2==0):
            break
        else:
            a = (a+1)//2
            b = (b+1)//2
            answer += 1

    return answer+1

#다른 사람 풀이

def solution(n,a,b):
    answer = 0
    while a != b:
        answer += 1
        a, b = (a+1)//2, (b+1)//2

    return answer
