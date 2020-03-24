global check

def DFS(i, computers):
    global check
    check[i] = 1

    for j in range(len(computers)):
        if check[j]:continue
        if computers[i][j]:
            DFS(j, computers)

def solution(n, computers):
    global check
    check = [0]*n
    answer = 0

    for i in range(n):
        if check[i]: continue
        DFS(i, computers)
        answer += 1
    return answer


print(solution(3,[[1, 1, 0],[1, 1, 0],[0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))