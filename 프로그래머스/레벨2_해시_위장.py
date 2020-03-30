import collections

def solution(clothes):
    answer = 1

    clothes = [i[1] for i in clothes]   # 모든 조합
    cnt_clothes = collections.Counter(clothes)  # 조합 개수 사전

    for i in list(cnt_clothes.values()):
        answer *= (i+1) # 미착용인 경우 하나 추가해서 순열

    return answer - 1   # 전부 미착용인 경우는 없으니 하나 빼줌

print(solution(	[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))