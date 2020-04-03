def solution(n, times):
    times.sort()
    l = 0
    r = times[0]*n
    answer = float('inf')

    while l<=r:
        mid = (l + r) // 2
        total = 0

        print(times, mid)

        for i in times:
            total += mid//i

        print(total)

        if total < n:
            l = mid+1
        else:
            if mid < answer:
                answer = mid
            r = mid-1

    return answer


print(solution(	6, [7, 10]))