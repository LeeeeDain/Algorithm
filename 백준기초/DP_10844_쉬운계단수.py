num = [[0 for _ in range(10)] for _ in range(100)]
num[0] = [0,1,1,1,1,1,1,1,1,1]

dp = [0]*100
dp[0] = 9

n = int(input())

for i in range(1, n):
    for j in range(0, 10):
        if j == 0:
            num[i][j] = num[i-1][1] %1000000000
        elif j == 9:
            num[i][j] = num[i-1][8] %1000000000
        else:
            num[i][j] = (num[i-1][j-1] + num[i-1][j+1]) %1000000000
    dp[i] = sum(num[i]) %1000000000

print(dp[n-1])
