from collections import deque

def solution(priorities, location):
    answer = 0

    d = deque([(j,i) for i,j in enumerate(priorities)])

    while len(d):
        select = d.popleft()
        if d and select[0] < max(d)[0]:
            d.append(select)
        else:
            answer += 1
            if select[1] == location:
                break
    return answer
