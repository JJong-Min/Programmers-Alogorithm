import math
def solution(str1, str2):
    answer = 0
    str1 = str1.upper()
    str2 = str2.upper()
    arr_str1 = {}
    arr_str2 = {}
    intersection_num = 0
    union_num = 0
    for i in range(len(str1)-1):
        if 'A'<=str1[i]<='Z' and 'A'<=str1[i+1]<='Z':
            if str1[i]+str1[i+1] in arr_str1.keys():
                arr_str1[str1[i]+str1[i+1]] += 1
            else:
                arr_str1[str1[i]+str1[i+1]] = 1
                
    for i in range(len(str2)-1):
        if 'A'<=str2[i]<='Z' and 'A'<=str2[i+1]<='Z':
            if str2[i]+str2[i+1] in arr_str2.keys():
                arr_str2[str2[i]+str2[i+1]] += 1
            else:
                arr_str2[str2[i]+str2[i+1]] = 1
    
    for i in arr_str1.keys():
        if i in arr_str2.keys():
            if arr_str1[i]>1 or arr_str2[i]>1:
                intersection_num += min(arr_str1[i], arr_str2[i])
                union_num += max(arr_str1[i], arr_str2[i])
            else:
                intersection_num += 1
                union_num += 1
        
        else:
            union_num +=  arr_str1[i]
    
    for i in arr_str2.keys():
        if i not in arr_str1:
            union_num += arr_str2[i]
    
    if union_num == 0:
        answer = 65536
    else:
        answer = math.floor(65536 * (intersection_num/union_num))
    return answer
