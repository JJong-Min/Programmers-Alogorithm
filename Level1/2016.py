def solution(a, b):
    answer = ''
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    if a == 1:
        answer = day[(b - 1)%7]
    elif a == 2:
        b = b + 31
        answer = day[(b - 1)%7]
    elif a == 3:
        b = b + 31 + 29
        answer = day[(b - 1)%7]
    elif a == 4:
        b = b+ 31 + 29 + 31
        answer = day[(b - 1)%7]
    elif a == 5:
        b = b+ 31 + 29 + 31 + 30
        answer = day[(b - 1)%7]
    elif a == 6:
        b = b+ 31 + 29 + 31 + 30 + 31
        answer = day[(b - 1)%7]
    elif a == 7:
        b = b+ 31 + 29 + 31 + 30 + 31 + 30
        answer = day[(b - 1)%7]
    elif a == 8:
        b = b+ 31 + 29 + 31 + 30 + 31 + 30 + 31
        answer = day[(b - 1)%7]
    elif a == 9:
        b = b+ 31 + 29 + 31 + 30 + 31 + 30 + 31 +31
        answer = day[(b - 1)%7]
    elif a == 10:
        b = b+ 31 + 29 + 31 + 30 + 31 + 30 + 31 +31 +30
        answer = day[(b - 1)%7]
    elif a == 11:
        b = b+ 31 + 29 + 31 + 30 + 31 + 30 + 31 +31 +30 +31
        answer = day[(b - 1)%7]
    elif a == 12:
        b = b+ 31 + 29 + 31 + 30 + 31 + 30 + 31 +31 +30 +31 +30
        answer = day[(b - 1)%7]    
    return answer
