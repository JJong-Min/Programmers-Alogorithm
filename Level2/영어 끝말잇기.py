def solution(n, words):
    answer = []
    perfect = True
    check_words = [words[0]]
    cnt = 0
    for i in range(1, len(words)):
        cnt+=1
        if words[i] not in check_words and words[i-1][-1] == words[i][0]:
            check_words.append(words[i])
        else:
            perfect = False
            break
    if perfect:
        answer = [0,0]
    else:
        answer.append((cnt%n)+1)
        answer.append((cnt//n)+1)
    return answer
