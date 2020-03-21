def solution(cacheSize, cities):
    check = list(i for i in range(0, cacheSize))
    cache = [0]*cacheSize
    time = 0

    if cacheSize == 0:
        return 5 * len(cities)

    for city in cities:
        city = city.lower()
        if city in cache:
            check.remove(cache.index(city))
            check.append(cache.index(city))
            time += 1
        else:
            cache[check[0]] = city
            tmp = check[0]
            check.remove(tmp)
            check.append(tmp)
            time += 5
    return time


print(solution(2,["Jeju", "Pangyo", "NewYork", "newyork"]))