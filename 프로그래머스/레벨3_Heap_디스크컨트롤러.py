import heapq

def solution(jobs):
    start = -1
    end = 0
    cnt = 0
    answer = 0
    n = len(jobs)
    h = []

    while cnt < n:
        for i in jobs:
            if start < i[0] <= end:
                heapq.heappush(h, i[1])
                answer += end - i[0]
        if len(h) > 0:
            print(len(h), h[0])
            answer += len(h) * h[0]
            start = end
            end += heapq.heappop(h)
            cnt += 1
        else:
            end += 1
    return answer//n


print(solution(	[[0, 3], [1, 9], [2, 6]]))
