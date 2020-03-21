from itertools import permutations
import math

# 소수 판정
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    r = int(math.sqrt(n))
    f = 5
    while f <= r:
        if n % f == 0 or n % (f + 2) == 0:
            return False
        f += 6
    return True


def solution(numbers):
    check_list = []
    answer_list = []
    answer = 0

    # numbers를 숫자 리스트로 변환
    numbers = list(int(numbers[i]) for i in range(len(numbers)))

    # check_list 구하기
    # check_list: numbers에서 가능한 모든 조합을 나타낸 튜플 리스트
    for i in range(1, len(numbers)+1):
        check_list.append(list(permutations(numbers, i)))

    # check_list 에서 하나씩 소수 검사
    # i: n개씩의 숫자조각 조합 모음
    # j: 숫자조각들
    # z: 숫자조각 하나
    for i in check_list:
        for j in i:
            # 숫자 조각들을 하나의 수(num)로 만들기
            num = 0
            ten = 1
            for z in list(j):
                num += ten*z
                ten *= 10
            # num이 이미 정답리스트에 있으면 패스
            if num in answer_list:
                continue
            # num이 소수인지 검사
            if is_prime(num) == True:
                answer_list.append(num)
                answer += 1

    return answer

print(solution("011"))