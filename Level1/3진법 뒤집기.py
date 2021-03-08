def solution(n):
    answer = 0
    Three = []
    while True:
        if n== 1 or n==2:
            break
        Three.append(n%3)
        n=n//3
    Three.append(n)
    j = len(Three)-1
    for i in range(len(Three)):
        answer += Three[i]*(3**j)
        j -= 1
    return answer
