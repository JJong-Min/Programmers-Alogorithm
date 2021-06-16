def solution(record):
    answer = []
    ans = []
    Enter = "님이 들어왔습니다."
    Leave = "님이 나갔습니다."
    nic = {}
    ids = []
    nicknames = []
    for i in record:
        arr = i.split()
       
        if arr[0] == 'Enter':
            nic[arr[1]] = arr[2]
            answer.append([arr[0], arr[1]])
        elif arr[0] == 'Leave':
            answer.append([arr[0], arr[1]])
        else:
            nic[arr[1]] = arr[2]
        

    for i in answer:
        if i[0] == "Enter":
    
            ans.append(nic[i[1]]+Enter)
        else:
            ans.append(nic[i[1]]+Leave)
  
    return ans
