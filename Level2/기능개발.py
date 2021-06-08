import math
from collections import deque
def solution(progresses, speeds):
    answer = []
    cnt = 0
    check = [ math.ceil((100 - x)/y) for x, y in zip(progresses, speeds)]
    q = deque(check)
    maximum = q[0]
    while q:
        a = q.popleft()
        maximum = max(maximum, a)
        cnt += 1
        if q == deque([]):
            answer.append(cnt)
        else:
            if maximum < q[0]:
                answer.append(cnt)
                cnt = 0
            else:
                continue     
    return answer
