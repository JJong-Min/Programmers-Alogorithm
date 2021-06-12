def solution(numbers, hand):
    left = [1,4,7]
    right = [3, 6, 9]
    middle = [2,5,8,0]
    left_position = (1,4)
    right_position = (3,4)
    answer = ''
    for number in numbers:
        if number in left:
            answer += 'L'
            left_position = (1, left.index(number)+1)
        elif number in right:
            answer += 'R'
            right_position = (3, right.index(number)+1)
        else:
            middle_idx = (2, middle.index(number)+1)
            if abs(left_position[0]-middle_idx[0])+abs(left_position[1]-middle_idx[1]) < abs(right_position[0]-middle_idx[0])+ abs(right_position[1]-middle_idx[1]):
                answer += 'L'
                left_position = middle_idx
            elif abs(left_position[0]-middle_idx[0])+abs(left_position[1]-middle_idx[1]) > abs(right_position[0]-middle_idx[0])+ abs(right_position[1]-middle_idx[1]):
                answer += 'R'
                right_position = middle_idx
            else:
                if hand == 'left':
                    answer += 'L'
                    left_position = middle_idx
                else:
                    answer += 'R'
                    right_position = middle_idx
                
    
    return answer
