# 내 풀이
def is_divisor(num):
    ans = 0
    for i in range(1, num+1):
        if num%i == 0:
            ans += 1
    if ans%2 == 0:
        return True
    else:
        return False
    
def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if is_divisor(i):
            answer += i
        else:
            answer -= i
    return answer


# 다른 사람 풀이
# 약수의 갯수가 홀수인 수는 제곱수가 정수
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer
