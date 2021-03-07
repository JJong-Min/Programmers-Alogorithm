def correct_num(answers, num):
    count = 0
    if len(answers)//len(num) == 0:
        for i in range(len(answers)):
            if answers[i] == num[i]:
                count += 1
    elif len(answers)//len(num) >0:
        a = len(answers)//len(num)
        num = num*a
        if len(answers)%len(num)>0:
            b = len(answers)%len(num)
            num = num+num[:b]
        for i in range(len(answers)):
            if num[i] == answers[i]:
                count += 1
    return count
def solution(answers):
    answer = []
    max1 = 0
    num1 = [1,2,3,4,5]
    num2 = [2, 1, 2, 3, 2, 4, 2, 5]
    num3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    if correct_num(answers, num1) == correct_num(answers, num2):
        answer.append(1)
        answer.append(2)
        max1 = correct_num(answers, num1)
    elif correct_num(answers, num1)>correct_num(answers, num2):
        answer.append(1)
        max1 = correct_num(answers, num1)
    else:
        answer.append(2)
        max1 = correct_num(answers, num2)
    if max1 == correct_num(answers, num3):
        answer.append(3)
    elif max1 < correct_num(answers, num3):
        answer = []
        answer.append(3)

    return answer
