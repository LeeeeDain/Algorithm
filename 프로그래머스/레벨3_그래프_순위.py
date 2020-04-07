import copy

def solution(n, results):
    answer = 0
    graph = [[] for _ in range(n+1)]
    result = [0]*n
    result_list = []

    for i in results:
        graph[i[0]].append(i[1])

    for i in range(1,n+1):
        child = copy.deepcopy(graph[i])
        add = []
        j = 0
        end = len(child)

        while j < end:
            a = child.pop(0)
            if a not in add:
                add.append(a)
                result[a-1] += 1
                child.extend(graph[a])
            j += 1
            if j == end:
                j = 0
                end = len(child)
        result_list.append(add)

    for i in range(n):
        if result[i-1] + len(result_list[i-1]) == n-1:
            answer += 1
    return answer


print(solution(	5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))