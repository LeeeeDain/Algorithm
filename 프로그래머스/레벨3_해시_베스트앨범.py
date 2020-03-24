def sum_plays(x):
    sum = 0
    for i in x:
        sum += i[0]
    return sum


def solution(genres, plays):
    answer = []
    best = []

    for index,genre in enumerate(genres):
        genre_list = []
        if genre != True:
            while genres.count(genre) > 0:
                index = genres.index(genre)
                genre_list.append([plays[index], index])
                genres[index] = True
            genre_list.sort(key=lambda x:x[0], reverse=True)
            answer.append(genre_list)

    answer.sort(key=lambda x: sum_plays(x), reverse=True)

    for genre in answer:
        try:
            best.append(genre[0][1])
            best.append(genre[1][1])
        except:
            continue

    return best

print(solution(	["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))