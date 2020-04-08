def solution(weight):
    answer = 0
    weight.sort()
    total = weight.pop(0)

    print(weight, total)
    for i in weight:
        if total+1 >= i:
            total += i
        else:
            return total+1
    return total+1


print(solution(	[3, 1, 6, 2, 7, 30, 1]))
print(solution([10,12,20]))