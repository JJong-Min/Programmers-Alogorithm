# 내 풀이
def solution(a, b):
    answer = 0
    length = len(a)
    for i in range(length):
        answer += a[i]*b[i]
    return answer 


#다른 사람 풀이
def solution(a, b):

    return sum([x*y for x, y in zip(a,b)])
