from collections import Counter

mystr = input()
cnt = Counter(mystr).most_common()

answer = ''
max_value = cnt[0][1]

for i in cnt:
    if i[1] == max_value:
        answer += i[0]

print(''.join(sorted(answer)))