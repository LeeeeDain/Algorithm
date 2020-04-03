def solution(heights):
    answer = []
    stack = []

    for index,height in enumerate(heights):
        result = 0
        while len(stack) > 0:
            before = stack.pop()-1
            if heights[before] <= height:
                continue
            else:
                result = before+1
                stack.append(before+1)
                break
        stack.append(index+1)
        answer.append(result)
    return answer

print(solution([6, 9, 5, 7, 4]))