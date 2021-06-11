# 내 풀이
def solution(absolutes, signs):
    answer = 0
    length = len(absolutes)
    for i in range(length):
        if signs[i] == True:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer


#다른 사람 풀이


def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))
