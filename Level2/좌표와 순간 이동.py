def solution(n):
    ans = 0
    while n >0:
        a, b = divmod(n, 2)
        n = a
        if b != 0:
            ans+=1
    
    return ans

#다른 사람 풀이 
def solution(n):
    return bin(n).count('1')
