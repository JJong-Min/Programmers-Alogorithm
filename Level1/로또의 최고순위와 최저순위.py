# 내 풀이
def solution(lottos, win_nums):
    answer = []
    ranks = { 0:6, 1:6, 2:5, 3:4, 4:3, 5:2, 6:1}
    cnt = 0
    zero_cnt = 0
    for i in lottos:
        if i == 0:
            zero_cnt += 1
        elif i in win_nums:
            cnt += 1
    answer.append(ranks[cnt+zero_cnt])
    answer.append(ranks[cnt])
    return answer


#다른 사람 풀이
def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]
