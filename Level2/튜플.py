# 내 풀이
def solution(s):
    answer = []
    ans= [[]]*1000001
    no = []
    idx = 0
    cnt = 0
    length = 0
    arr = s[1:-1].split(",")
    if len(arr) == 1:
        return [int(arr[0][1:-1])]
    
    for i in arr:
        if cnt == 2:
            ans[idx] = no
            length = max(length, idx)
            idx = 0
            cnt = 0
            no = []
        if i[0] == '{' and i[-1] == '}':
            ans[1] = [int(i[1:-1])]
        elif i[0] == '{':
            idx += 1
            cnt += 1
            no.append(int(i[1:]))
        elif i [-1] == '}':
            idx += 1
            cnt += 1
            no.append(int(i[:-1]))
        else:
            no.append(int(i))
            idx += 1
    ans[idx] = no
    length = max(length, idx)
    
    for i in ans[:length+1]:
        for j in i:
            if j not in answer:
                answer.append(j)
    return answer



# 다른 사람 풀이
def solution(s):
    answer = []

    s1 = s.lstrip('{').rstrip('}').split('},{')

    new_s = []
    for i in s1:
        new_s.append(i.split(','))

    new_s.sort(key = len)

    for i in new_s:
        for j in range(len(i)):
            if int(i[j]) not in answer:
                answer.append(int(i[j]))

    return answer
