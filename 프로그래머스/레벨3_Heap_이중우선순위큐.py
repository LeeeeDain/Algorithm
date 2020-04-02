import heapq

def solution(operations):
    h = []

    for oper in operations:
        if oper[0] == 'I':
            heapq.heappush(h, int(oper[2:]))
        elif oper == 'D 1' and len(h) > 0:
            h.remove(max(h))
        elif oper == 'D -1' and len(h) > 0:
            heapq.heappop(h)

    if not h:
        return [0,0]
    return [max(h), h[0]]
