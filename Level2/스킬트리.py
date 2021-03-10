def solution(skill, skill_trees):
    answer = 0
    for i in range(len(skill_trees)):
        skill_list = list(skill)
        skill_check = [0]*(len(skill)+1)
        for j in skill_trees[i]:
            if j not in skill:
                skill_check[-1 ] += 1
            else:
                if skill_check[skill_list.index(j)-1] == 1 or skill_list.index(j) == 0:
                    skill_check[skill_list.index(j)] += 1
                    print(skill_check)
                else: 
                    break
            if j == skill_trees[i][-1]:
                answer += 1
            
            
            
    return answer
