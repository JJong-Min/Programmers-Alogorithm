def solution(N, stages):
    answer = []
    fails = []
    users = len(stages)
    for i in range(1, N+1):
        if users != 0:
            none_clear_stage = stages.count(i)
            fails.append((i, (none_clear_stage/users)))
            users -= none_clear_stage
        else:
            fails.append((i, 0))
    fails = sorted(fails, key = lambda x: x[1], reverse = True)
    for i in fails:
        answer.append(i[0])
    return answer
