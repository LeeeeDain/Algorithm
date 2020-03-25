import heapq as hq

def solution(stock, dates, supplies, k):
    answer = 0
    index = 0
    heap = []

    while stock < k:
        while index < len(dates):
            if dates[index] <= stock:
                hq.heappush(heap,(-supplies[index], supplies[index]))
                index += 1
            else:
                break
        stock += hq.heappop(heap)[1]
        answer += 1
    return answer



print("**",solution(	4, [4, 10, 14, 15], [20, 5, 5, 10], 30))
print("**",solution(4,[3],[4],5))
print("**",solution(1,[1,2,3,4],[1,1,1,100],20))
print("**",solution( 4, [1, 2, 3, 4,5], [1, 40, 30, 20,9], 100))