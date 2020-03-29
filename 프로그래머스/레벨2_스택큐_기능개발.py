import math

def solution(progresses, speeds):
    answer = []

    works= []

    for i in range(len(progresses)):
        works.append(math.ceil((100-progresses[i])/speeds[i]))

    max = works.pop(0)
    cnt = 1
    for i in works:
        if max >= i:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            max = i

    answer.append(cnt)

    return answer


print(solution(	[93, 30, 55], [1, 30, 5]))