# A~M / N~Z 로 나눠서 차이 구하는 함수
def alphabetCheck(character):
    if character < "N":
        return ord(character) - ord("A")
    else:
        return ord("Z") - ord(character) + 1

def solution(name):
    answer = 0  # 조이스틱 횟수
    now = 0     # 현재 인덱스 위치
    check = []

    # check: A가 아닌 문자들 인덱스 리스트
    for i in range(len(name)):
        if name[i] != "A":
            check.append(i)

    # check가 빌 때까지 검사
    while len(check) > 0:
        # check[0]을 선택하면 무조건 right 방향
        # check[1]을 선택하면 무조건 left 방향

        # 1. now가 check[0] 보다 작은 경우, 큰 경우로 나눠서 거리차이 계산
        if now <= check[0]:
            right = check[0] - now
        else:
            right = check[0] - 0 + len(name) - now

        # 2. now가 check[-1] 보다 작은 경우, 큰 경우로 나눠서 거리차이 계산
        if now <= check[-1]:
            left = len(name) - check[-1] + now
        else:
            left = now - check[-1]

        # 3. right, left 거리 비교 후 조이스틱 횟수 계산
        # 선택한 원소는 check에서 지우고 now 갱신
        if right <= left:
            answer += right
            answer += alphabetCheck(name[check[0]])
            now = check[0]
            check.remove(check[0])
        else:
            answer += left
            answer += alphabetCheck(name[check[-1]])
            now = check[-1]
            check.remove(check[-1])

    return answer

print(solution("AA"))