def solution(answers):
    n = len(answers)
    one = [1,2,3,4,5] * (int(n/5)+1)
    two = [2,1,2,3,2,4,2,5] * (int(n/8)+1)
    thr = [3,3,1,1,2,2,4,4,5,5] * (int(n/10)+1)

    cnt = [0,0,0]

    for index,value in enumerate(answers):
        if value == one[index]: cnt[0] += 1
        if value == two[index]: cnt[1] += 1
        if value == thr[index]: cnt[2] += 1

    max_cnt = max(cnt)
    max_list = [index+1 for index, value in enumerate(cnt) if value == max_cnt]
    return max_list


print(solution([1,2,3,4,5]))