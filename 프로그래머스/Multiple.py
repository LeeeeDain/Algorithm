import math

def primeSieve(sieveSize):
    # creating Sieve (0~n까지의 slot)
    sieve = [True] * (sieveSize+1)
    # 0과 1은 소수가 아니므로 제외
    sieve[0] = False
    sieve[1] = False
    # 2부터 (루트 n) + 1까지의 숫자를 탐색
    for i in range(2,int(math.sqrt(sieveSize))+1):
        # i가 소수가 아니면 pass
        if sieve[i] == False:
            continue
        # i가 소수라면 i*i~n까지 숫자 가운데 i의 배수를
        # 소수에서 제외
        for pointer in range(i**2, sieveSize+1, i):
            sieve[pointer] = False
    primes = []
    # sieve 리스트에서 True인 것이 소수이므로
    # True인 값의 인덱스를 결과로 저장
    for i in range(sieveSize+1):
        if sieve[i] == True:
            primes.append(i)
    return primes

def factor(n):
    # n 범위 내의 소수를 구한다
    primelist = primeSieve(n)
    # 이 소수들 중 n으로 나누어 떨어지는
    # 소수를 구하고, 몇 번 나눌 수 있는지 계산
    # 예 : n = 8, factors = [(2, 3)]
    # 예 : n = 100, fcount = [(2: 2), (5: 2)]
    factors = {}
    for p in primelist:
        count = 0
        while n % p == 0:
            n /= p
            count += 1
        if count > 0:
            factors[p] = count
    return factors

def solution(arr):
    answer = 1
    factorList = {}

    for num in arr:
        dic = factor(num)
        for key in dic:
            if factorList.get(key) == None:
                factorList[key] = dic.get(key)
            elif factorList.get(key) < dic.get(key):
                factorList[key] = dic.get(key)

    for key in factorList.keys():
        answer = answer * (key**factorList.get(key))

    print(answer)

    return answer


solution([2,6,8,14])