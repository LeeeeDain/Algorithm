def solution(citations):
    return max(map(min, enumerate(sorted(citations, reverse=True), start=1)))

print(solution([1,0]))
print(solution([3,6]))
print(solution([3, 0, 6, 1, 5]))