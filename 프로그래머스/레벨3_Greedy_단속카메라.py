def solution(routes):
    answer = 0
    camera = float('-inf')
    routes.sort(key=lambda x: x[1])
    for i in routes:
        if camera < i[0]:
            camera = i[1]
            answer += 1
    return answer


print(solution(	[[-20, 15], [-14, -5], [-18, -13], [-5, -3]]))