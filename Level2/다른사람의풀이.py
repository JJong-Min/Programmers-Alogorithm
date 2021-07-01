#다른 사람 풀이
def solution(s):
    a, b = 0, 0
    while s != '1':
        a += 1
        num = s.count('1')
        b += len(s) - num
        s = bin(num)[2:]
    return [a, b]

# 내 풀이 
from collections import deque
def bfs(s, zero_cnt):
    queue = deque([s])
    cnt = 0
    while queue:
        s = queue.popleft()
        if s == '1':
            break
        else:
            cnt +=1
            new_s = ''
            for i in s:
                if i == '1':
                    new_s += i
                else:
                    zero_cnt += 1
        new_s = bin(len(new_s))[2:]
        queue.append(new_s)
    return cnt, zero_cnt           
def solution(s):
    answer = []
    s = list(s)
    zero_cnt = 0
    answer.append(bfs(s, zero_cnt)[0])
    answer.append(bfs(s, zero_cnt)[1])
                
    return answer
