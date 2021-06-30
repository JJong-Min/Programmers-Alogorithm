# 다른사람 풀이
def solution(numbers):
    answer = [] 
    for number in numbers: 
        if number % 2 == 0: 
            binary_num = list(bin(number)[2:]) 
            binary_num[-1] = "1" 
        else: 
            binary_num = bin(number)[2:] 
            binary_num = "0" + binary_num 
            one_idx = binary_num.rfind("0") 
            binary_num = list(binary_num) 
            binary_num[one_idx] = "1" 
            binary_num[one_idx + 1] = "0" 
        ans_num = int("".join(binary_num), 2) 
        answer.append(ans_num) 
    return answer

# 내 풀이(시간 초과)
def solution(numbers):
    answer = []
    for i in numbers:
        i_binary = bin(i)[2:]
        while True:
            i+=1
            cnt = 0
            next_binary = bin(i)[2:]
            len_i = len(i_binary)
            len_next = len(next_binary)
            if len_i< len_next:
                i_binary = '0'*(len_next-len_i) + i_binary
            for j in range(len_next):
                if next_binary[j] != i_binary[j]:
                    cnt += 1
            if cnt <=2:
                break
        answer.append(i)
    return answer
