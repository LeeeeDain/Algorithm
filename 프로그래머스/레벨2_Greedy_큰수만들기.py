def solution(number, k):
    answer = ''
    now = len(number) - 1 - k

    while now > 0:
        check_number = number[:-now]

        for i in reversed(range(10)):
            if str(i) in check_number:
                index = check_number.index(str(i))
                break

        answer = answer + number[index]
        number = number[index+1:]
        now -= 1

    answer = answer + max(number)

    return answer


print(solution("99490", 2))