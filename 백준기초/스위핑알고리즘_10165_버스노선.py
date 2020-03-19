from operator import itemgetter
import sys

arr1 = []
arr2 = []
arr2_min_a = 1e9
arr2_max_b  = -1

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

for i in range(1,m+1):
    a, b = map(int, sys.stdin.readline().split())
    a = int(a)
    b = int(b)

    if a < b:
        arr1.append([a,-b,i])
    else:
        arr2_min_a = min(arr2_min_a, a)
        arr2_max_b = max(arr2_max_b, b)
        arr2.append([a,-(n+b),i])

sorted(arr1, key=itemgetter(0,1))
sorted(arr2, key=itemgetter(0,1))

busList = []

max_b = -1
for bus in arr1:
    a = bus[0]
    b = -bus[1]
    i = bus[2]
    if a >= arr2_min_a: continue
    if b <= arr2_max_b: continue
    if b <= max_b: continue
    max_b = b
    busList.append(i)

max_b = -1
for bus in arr2:
    a = bus[0]
    b = -bus[1]
    i = bus[2]
    if b <= max_b: continue
    max_b = b
    busList.append(i)

for i in busList:
    print(str(i), end = ' ')