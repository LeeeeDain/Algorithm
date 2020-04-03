def solution(budgets, M):
    if sum(budgets) <= M:
        return max(budgets)

    answer = 0
    l = 1
    r = max(budgets)
    mid = 0

    while l<=r:
        mid = (l+r)//2
        total = 0

        for i in budgets:
            if i <= mid:
                total += i
            else:
                total += mid

        if total > M:
            r = mid - 1
        else:
            if answer < mid:
                answer = mid
            l = mid + 1

    return answer


print(solution(	[120, 110, 140, 150], 485))