def solution(n, costs):
    answer = 0
    costs.sort()
    connect = [costs[0][0]]

    while len(connect) < n:
        candidate = []
        for i in connect:
            for j in costs:
                if (i == j[0] and j[1] not in connect)\
                        or (i == j[1] and j[0] not in connect):
                    candidate.append(j)
        min_cost = min(candidate, key=lambda x:x[2])
        answer += min_cost[2]
        connect.append(min_cost[0])
        connect.append(min_cost[1])
        connect = list(set(connect))
        costs.remove(min_cost)
    return answer



print(solution(	5, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 4],[4,3,8]]))
print(solution(	4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))
print(solution(	4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 1]]))
print(solution( 5, [[0,1,1],[0,2,2],[1,2,5],[1,3,3],[2,3,8],[3,4,1]] ))