n = int(input())
num_list = [int(input()) for _ in range(n)]
dp = []

if n <= 2:
    dp.append(sum(num_list))
else:
    dp.append(num_list[0])
    dp.append(num_list[0] + num_list[1])
    dp.append(max(dp[0] + num_list[2], num_list[1] + num_list[2]))

    for i in range(3, n):
        dp.append(max(num_list[i] + num_list[i - 1] + dp[i - 3], num_list[i] + dp[i - 2]))

print(dp[-1]) 