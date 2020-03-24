import heapq as hq

def solution(scoville, K):
    answer = 0
    hq.heapify(scoville)

    while len(scoville) >= 2:
        if scoville[0] >= K:
            return answer
        hq.heappush(scoville, hq.heappop(scoville) + hq.heappop(scoville)*2)
        answer += 1

    if scoville[0] >= K:
        return answer
    return -1


#print(solution(	[1, 1, 8], 7))
#print(solution([2,1,3,4, 10, 12]	,7))
#print(solution([10,0,0,0,5,10],2))
print(solution([1,2,6,5,4,100000],100000))