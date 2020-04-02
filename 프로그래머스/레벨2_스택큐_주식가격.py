def solution(prices):
    answer = [0] * len(prices)
    s = []

    for idx, val in enumerate(prices):
        while s and s[-1][0] > val:
            n = s.pop()
            answer[n[1]] = idx - n[1]
        s.append((val, idx))

    while len(s):
        n = s.pop()
        answer[n[1]] = len(prices) - 1 - n[1]

    return answer