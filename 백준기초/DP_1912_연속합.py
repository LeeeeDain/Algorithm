n = int(input())
num_list = list(map(int, input().split()))
max_num = -1001
temp = [0]*n

for i in range(n):
    temp[i] = max(temp[i-1]+num_list[i], num_list[i])
    max_num = max(max_num, temp[i])

print(max_num)