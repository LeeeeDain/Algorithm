def solution(distance, rocks, n):
    if n == len(rocks):
        return distance

    rocks.append(0)
    rocks.append(distance)
    rocks.sort()

    l = 0
    r = distance
    answer = 0

    d = []
    for i in range(len(rocks)-1):
        d.append(rocks[i+1]-rocks[i])

    while l<=r:
        add = 0
        cnt = 0
        mid = (l+r)//2
        for i in d:
            if i+add < mid:
                cnt += 1
                add +=i
            else:
                add = 0

        if cnt > n:
            r = mid - 1
        else:
            answer = mid
            l = mid + 1

    return answer



print(solution(	25, [2, 14, 11, 21, 17], 1))