global graph, distance

def solution(n, edge):
    global graph, distance
    graph = [[] for i in range(n)]
    distance = [0] * n

    for i in edge:
        graph[i[0]-1].extend([i[1]])
        graph[i[1]-1].extend([i[0]])

    cnt = 1
    q = [1]
    n = len(q)
    i = 0

    while i < n:
        start = q.pop(0)
        if distance[start-1] == 0:
            distance[start-1] = cnt
            q.extend(graph[start-1])
        i += 1
        if i == n:
            n = len(q)
            i = 0
            cnt += 1
    return distance.count(max(distance))


print(solution(	6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))