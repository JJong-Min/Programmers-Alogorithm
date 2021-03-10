from collections import deque
def solution(priorities, location):
    answer = 0
    prioritie = []
    for i in range(len(priorities)):
        prioritie.append((priorities[i], i))
    priorities.sort(reverse = True)
    q = deque(prioritie)
    while q:
        a = q.popleft()
        if a[0] >= priorities[0]:
            if a[1] == location:
                answer += 1
                break
            else:
                answer += 1
                del priorities[0]
        else:
            q.append(a)   
    return answer
