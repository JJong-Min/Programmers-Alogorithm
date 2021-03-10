def solution(nums):
    if len(list(set(nums))) < len(nums) // 2:
        return len(list(set(nums)))
    return len(nums) // 2
