from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    people = deque(people)

    while len(people):
        n = people.pop()
        for i in range(len(people)):
            if n+people[i] > limit:
                break
            else:
                people.remove(people[i])
                break
        answer += 1
    return answer



print(solution(	[70, 50, 80, 50], 100))
print(solution(	[70,30,70,30], 100))
