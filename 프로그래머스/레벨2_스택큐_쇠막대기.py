from collections import deque

def solution(arrangement):
    answer = 0
    s = 0
    arrangement = deque(arrangement.replace('()','0'))

    while len(arrangement):
        now = arrangement.popleft()
        if arrangement and now == '0':
            answer += s
        elif now == '(':
            s += 1
        else:
            s -= 1
            answer += 1

    return answer


print(solution("()(((()())(())()))(())"))