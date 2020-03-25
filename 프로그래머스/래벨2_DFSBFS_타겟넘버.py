def solution(numbers, target):
    answer_list = [0]
    for i in numbers:
        answer_list = list(map(lambda x: x+i, answer_list)) + list(map(lambda x: x-i, answer_list))
    return answer_list.count(target)

print(solution([1,1,1,1,1],3))