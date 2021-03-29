# 첫 번째 시도(효율성 테스트 시간초과)
def solution(phone_book):
    answer = True
    for i in range(len(phone_book)):
        phone_num = phone_book[i]
        for idx in range(len(phone_book)):
            if i == idx:
                continue
            if phone_num == phone_book[idx][:len(phone_num)]:
                answer = False
                break
    return answer


# sort()함수 활용, for문 1개만 사용해서 가능
def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            answer = False
            break
    return answer
