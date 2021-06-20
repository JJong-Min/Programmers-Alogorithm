def except_not_allowance(string):
    ans = ''
    for i in string:
        if i.isalnum() or i in '-_.':
            ans += i
    return ans
def switch_dots(string):
    while '..' in string:
        string = string.replace('..', '.')
    return string

def solution(new_id):
    new_id = new_id.lower()
    new_id = except_not_allowance(new_id)
    new_id = switch_dots(new_id)
    new_id = new_id.lstrip('.')
    new_id = new_id.rstrip('.')
    if new_id == '':
        new_id = 'a'
    if len(new_id) >=16:
        new_id = new_id[:15]
        new_id = new_id.rstrip('.')
    if len(new_id) <=2:
        new_id = new_id + new_id[-1]*(3-len(new_id))
    
    return new_id
