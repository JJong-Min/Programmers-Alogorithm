from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_on_bridge = []
    truck_on_time = []
    q = deque(truck_weights)
    while q:
        answer += 1
        if truck_on_time != [] and answer - int(truck_on_time[0]) == bridge_length:
            del truck_on_bridge[0]
            del truck_on_time[0]
        if sum(truck_on_bridge) + int(q[0]) <= weight:
            a = q.popleft()
            truck_on_bridge.append(a)
            truck_on_time.append(answer)
        else:
            continue 
            
    answer += bridge_length    
    return answer
