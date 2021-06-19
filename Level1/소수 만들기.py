def comb(population,num):
	ans = []
    ## 정의된 값인지 확인한다.
	if num > len(population): return ans
	## Base Case
	if num == 1:
		for i in population:
			ans.append([i])
    ## General Case
	elif num>1:
		for i in range(len(population)-num+1): ## i가 시작하는 값 - len(population) - (n-1)이고 이 때 n은 lst로부터 추출할 개수와 같다.
			for temp in comb(population[i+1:],num-1):
				ans.append([population[i]]+temp)

	return ans

def is_prime_num(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(x**(1/2)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임

def solution(nums):
    answer = 0
    candidate = comb(nums, 3)
    for i in candidate:
        CandidateOfPrimeNum = sum(i)
        if is_prime_num(CandidateOfPrimeNum):
            answer += 1



    
    return answer
