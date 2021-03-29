def solution(s):
    answer = 9999
    for i in range(1, len(s)+1):
        new_s = ''
        count = 1
        array = ''
        for j in range(0,len(s),i):
            if j == 0:
                array = s[j:j+i]
                continue
            if array == s[j:j+i]:
                count+=1
            else:
                if count>1:
                    new_s += str(count)
                    new_s += array
                    count = 1
                    array = s[j:j+i]
                else:
                    new_s += array
                    array = s[j:j+i]
        if count == 1:
            new_s += array
        else:
            new_s += str(count)
            new_s += array
        answer = min(answer, len(new_s))

    return answer
