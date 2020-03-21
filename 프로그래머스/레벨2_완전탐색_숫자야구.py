from itertools import permutations

def solution(baseball):
    answer = 0
    check_list = list(permutations([1,2,3,4,5,6,7,8,9],3))

    for check_num in check_list:
        check_num = (list(check_num))
        success = 0

        for test in baseball:
            num = str(test[0])
            ball = 0
            strike = 0
            for i in range(3):
                if num[i] in str(check_num):
                    ball += 1
                if int(num[i]) == int(check_num[i]):
                    ball -= 1
                    strike += 1

            if test[1] == strike and test[2] == ball:
                success += 1
            else:
                break

        if success == len(baseball):
            answer += 1

    return answer

print(solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]))